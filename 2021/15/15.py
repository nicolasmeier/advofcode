import re
import numpy as np
import math
import functools
import collections 

import os
import sys
os.chdir(os.path.dirname(sys.argv[0]))

li = []
with open("15t.txt") as f:
    li = [x.strip() for x in f.readlines()]

b = []
for l in li:
    b.append([int(x) for x in l])
#b = np.array(b)

class Graph():
 
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
 
    def printSolution(self, dist):
        print("Vertex tDistance from Source")
        for node in range(self.V):
            print(node, "t", dist[node])
 
    # A utility function to find the vertex with
    # minimum distance value, from the set of vertices
    # not yet included in shortest path tree
    def minDistance(self, dist, sptSet):
 
        # Initialize minimum distance for next node
        min = sys.maxsize
 
        # Search not nearest vertex not in the
        # shortest path tree
        for v in range(self.V):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v
 
        return min_index
 
    # Function that implements Dijkstra's single source
    # shortest path algorithm for a graph represented
    # using adjacency matrix representation
    def dijkstra(self, src):
 
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V
 
        for cout in range(self.V):
 
            # Pick the minimum distance vertex from
            # the set of vertices not yet processed.
            # u is always equal to src in first iteration
            u = self.minDistance(dist, sptSet)
 
            # Put the minimum distance vertex in the
            # shortest path tree
            sptSet[u] = True
 
            # Update dist value of the adjacent vertices
            # of the picked vertex only if the current
            # distance is greater than new distance and
            # the vertex in not in the shortest path tree
            for v in range(self.V):
                if (self.graph[u][v] > 0 and
                   sptSet[v] == False and
                   dist[v] > dist[u] + self.graph[u][v]):
                        dist[v] = dist[u] + self.graph[u][v]
 
        self.printSolution(dist)

g = Graph(len(b))
g.graph = b
 
g.dijkstra(0)
quit()
print(b)
mincost = np.sum(b[0]) + np.sum(b.T[-1][1:])

def findPath(b,x,y,seen,cost):
    if (x,y) in seen: return 99999999999
    if x == len(b)-1 and y == len(b[0])-1: return cost + b[x][y]
    if not (0 <= x < len(b)): return 9999999999
    if not (0 <= y < len(b[0])): return 99999999999
    if cost > mincost: return 99999999999
    seen = seen | {(x,y)}
    n = findPath(b,x+1,y,seen,cost + b[x][y])
    s = findPath(b,x-1,y,seen,cost + b[x][y])
    e = findPath(b,x,y+1,seen,cost + b[x][y])
    w = findPath(b,x,y-1,seen,cost + b[x][y])
    return min(n,s,w,e)
        
print(findPath(b,0,0,set(),0))