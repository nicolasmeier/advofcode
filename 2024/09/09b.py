import os
import sys
import numpy as np

# Run where the script is
os.chdir(os.path.dirname(sys.argv[0]))

def trans(x: str):
    return list(map(int, [y for y in x]))

# Read and process the input file
li = []
with open("09.txt") as f:
    li = [trans(x.strip()) for x in f.readlines()]

# Extract the first line of input
d = li[0]

# Create the initial list `b` as in Part 1
b = []
b2 = []
empty = False
iii = 0
for m in d:
    if empty:
        b2.append(('.', m))
        for _ in range(m):
            b.append('.')
    else:
        b2.append((str(iii), m))
        for _ in range(m):
            b.append(str(iii))
        iii += 1
    empty = not empty

# Identify file blocks and free spaces
files = {}
current_file = None
start_idx = None

# Parse file positions from `b`
for i, slot in enumerate(b):
    if slot != '.' and slot != current_file:
        if current_file is not None:
            files[current_file] = (start_idx, i - start_idx)
        current_file = slot
        start_idx = i
    elif slot == '.' and current_file is not None:
        files[current_file] = (start_idx, i - start_idx)
        current_file = None

if current_file is not None:
    files[current_file] = (start_idx, len(b) - start_idx)

# Process files in descending order of file ID
for file_id in sorted(files.keys(), key=lambda x: int(x) if x.isdigit() else -1, reverse=True):
    start, length = files[file_id]

    # Find the leftmost span of free space that can fit the file (to the left of the current position)
    free_space_start = None
    free_space_length = 0
    for i, slot in enumerate(b):
        if slot == '.':
            if free_space_start is None:
                free_space_start = i
            free_space_length += 1
        else:
            free_space_start = None
            free_space_length = 0

        # Check if the span ends before the file's original position
        if free_space_length >= length and (free_space_start + free_space_length) <= start:
            # Move the file
            b[start:start + length] = ['.'] * length
            b[free_space_start:free_space_start + length] = [file_id] * length
            files[file_id] = (free_space_start, length)  # Update file's position
            break

# Calculate the checksum (Part 2)
part2 = 0
for i, slot in enumerate(b):
    if slot != '.':
        part2 += i * int(slot)

print(f"Part2= {part2}")
