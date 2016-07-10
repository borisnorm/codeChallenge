#Implement hSort
from heapq import *
h = []
heappush(h, 4)
heappop(h)

def heap_sort(array):
  h = []
  solution = []
  while (array):
    heappush(h, array.pop())
  while (h):
    solution.append(heappop(h))
  return solution

test = [1, 2, 3, 4, 5, 6, 7]
print heap_sort(test)
