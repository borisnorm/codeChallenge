#find the mst, based on each vertex keep on finding the closest vertex not visited till done

from heapq import *

def prims(source, graph):
  h = []
  solution = []
  heappush(h, source)
  size = len(graph.keys())
  visited = set()
  source = source

  while len(visited) < size:
    item = heappop(h)
    if item not in visited:
      solution.append(source, item, distance(source, item))
      visited.add(item)
      for nodes in getNeighbors(item):
        heappush(h, (distance(item, nodes), nodes)) #assumes edges are recieved
      source = item
  return solution


