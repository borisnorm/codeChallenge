 #BFS
 #The graph just needs to have some time of get neighbors function
 #get Neighbors function, to return and array

 def graph_neighbors(node, graph):
   return graph[node]

 #Keep track of the specific x and y items
 def matrix_neighbors(item, matrix, lookup):
   neighbors = []
   item = lookup(item)
   x = item[0]
   y = item[1]
   for i in range(-1 + x, x + 2):
     for j in range(-1 + y, y + 2):
       if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix):
         pass
       else:
         if (i is not x) and (j is not y):
           neighbors.append(matrix[i][j])
   return neighbors

#implement with the has lookup
def lookup = {}
for i in len(matrix):
  for j in len(matrix[0])
    lookup[matrix[i][j]] = (i, j)

def dfs(source, target, graph):
  stack = [source]
  while (stack):
    item = stack.pop(0)
    if item == target:
      return True
    for item in matrix_neighbors(item, matrix, lookup):
      stack.insert(0, item)
  return False
