#!/usr/bin/env python3

from collections import defaultdict, Counter
from functools import lru_cache
import itertools
import math
import string
import sys
import unittest


import os
import sys
os.chdir(os.path.dirname(sys.argv[0]))

class Tests(unittest.TestCase): # no tests lol
	def setUp(self):
		self.testinput = """"""
		self.test = parse_input(self.testinput.split("\n"))
	
	def test_part1(self):
		#self.assertEqual(part1(self.test), y)
		pass
		
	def test_part2(self):
		#self.assertEqual(part2(self.test), y)
		pass

def parse_input(i):
	out = []
	for line in i:
		out.append(tuple(line.strip().split()))
	return tuple(out)

BLOCK_SIZE = 18

@lru_cache()
def eval_block(block, digit, z0):
	"""Evaluates a single block with a given digit and z0, determining the z0 afterwards"""
	x = 0 if ((z0 % 26) + int(block[5][2])) == digit else 1
	z = z0 // int(block[4][2])
	z1 = z * ((25 * x) + 1)
	z2 = z1 + (x * (digit + int(block[15][2])))
	return z2

@lru_cache()
def recursive_block(prog, idx, z0, rb):
	"""Recursively determines the largest sequence of digits necessary to run the rest of the program with z = z0 to start, and ending with z = 0"""
	if idx + BLOCK_SIZE >= len(prog):
		for i in range(9, 0, -1):
			if eval_block(prog[idx:], i, z0) == 0:
				return i
		return 0
	else:
		if prog[idx + 4][2] == "1":
			# inc block
			rng = range(9, 0, -1)
		else:
			# dec block
			x = z0 % 26
			x += int(prog[idx + 5][2])
			if x <= 0 or x > 9:
				return 0
			rng = range(x, x + 1)
		for i in rng:
			val = int(prog[idx + 5][2])
			res = recursive_block(prog, idx + BLOCK_SIZE, eval_block(prog[idx:idx + BLOCK_SIZE], i, z0), rb - 1)
			if res > 0:
				return (i * (10 ** rb)) + res
		return 0
	return 0
	

@lru_cache()
def recursive_block_2(prog, idx, z0, rb):
	"""Recursively determines the smallest sequence of digits necessary to run the rest of the program with z = z0 to start, and ending with z = 0"""
	if idx + BLOCK_SIZE >= len(prog):
		for i in range(1, 10):
			if eval_block(prog[idx:], i, z0) == 0:
				return i
		return 0
	else:
		if prog[idx + 4][2] == "1":
			# inc block
			rng = range(1, 10)
		else:
			# dec block
			x = z0 % 26
			x += int(prog[idx + 5][2])
			if x <= 0 or x > 9:
				return 0
			rng = range(x, x + 1)
		for i in rng:
			val = int(prog[idx + 5][2])
			res = recursive_block_2(prog, idx + BLOCK_SIZE, eval_block(prog[idx:idx + BLOCK_SIZE], i, z0), rb - 1)
			if res > 0:
				return (i * (10 ** rb)) + res
		return 0
	return 0

def part1(i):
	return recursive_block(i, 0, 0, 13)

def part2(i):
	return recursive_block_2(i, 0, 0, 13)

def main():
	with open("24.txt", "r") as f:
		i = parse_input(f.readlines())
	print(part1(i))
	print(part2(i))

if __name__ == '__main__':
	main()