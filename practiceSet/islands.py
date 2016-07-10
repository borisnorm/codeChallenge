#Iterate regularly through everything
  #if two things are adjacent add them into the same set
  #return the number of disjoint sets

#Second approach
  #ALways set adjacent islands to the same number and then count the islands

#Use some type of DFS search
 #DFS can work for marking,
  #dont initalize DFS if it has been visited alreayd with a set
  #IF DFS, is then done, update the counter to a different type

def getNeighbors(matrix, x, y):
  neighbors = []
  for i in range(x - 1, x + 2):
    for j in range(y - 1, y + 2):
      if (x < 0 or y < 0 or x > len(matrix) or y > len(matrix)):
        print "reject case"
      else:
        #check to see if certain things work here
        neighbors.append((matrix[x][y], x, y))
  return neigbors
  #Modify certain rejection cases

#I need to add that to the visitng - maybe there are two different sets that i need to work on
def DFS_marker(root, matrix, marking, visited):
  que = [root]
  while (que):
    item = que.pop()
    if item not in visited:
      visited.add(item)
      if item[0] > 0:
        print "pass"
      else:
        matrix[item[1]][item[2]] = marking
        que.insert(getNeighbors(root), 0)
  marking++
  return

def findIslands(matrix):
  visited = Set()
  marking = 0;
  for i in range(0, len(matrix)):
    for j in range(0, len(matrix)):
      if matrix[x][y] < 1:
        next
      else:
        DFS_marker((matrix[i][j], i, j), matrix, marking, visited)
  #Scan the arraay for unique entries
  return marking

