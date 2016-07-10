#BFS

#The graph just needs to have some time of get neighbors function
#get Neighbors function, to return and array

def graph_neighbors(node, graph):
  return graph[node]

#Keep track of the specific x and y items
def matrix_neighbors(item, matrix):
  neighbors = []
  x = item[1]
  y = item[2]
  for i in range(-1 + x, x + 2):
    for j in range(-1 + y, y + 2):
      if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix):
        pass
      else:
        if (i is not x) and (j is not y):
          neighbors.append((matrix[i][j], i, j))
  return neighbors

def bfs(source, target, graph):
  queue = [source]
  while queue:
    item = queue.pop()
    if item[0] == target:
      return True
    for item in getNeighbors(item):
      queue.insert(0, item)
  return False
