#See if matrix contains a particular word

#DFS but custom implementation

#Adding padding function here, with a new matrix there
  #are other things to work on

def getNeighbors(x, y, matrix):
  #I had for i in range(i - 1, i + 2), my ranges should be dealing with Xs and not anything else!
  neighbors = []
  for i in range(x - 1, x + 2):
    for j in range(y - 1, y + 2):
      #Change this if it is not square
      if (i < 0 or j < 0 or j > len(matrix) or i > len(matrix)):
        print "edge case"
      else:
        neighbors.append((matrix[x][y], i, j))
  return neighbors


def DFS(root, target):
  visit = Set()
  path = ''
  que = [root]
  while (que):
      item = que.pop()
      if item not in visit:
        path.append(root[0])
        visit.insert(item, 0)
        #There are different types of add
        #append adds the object, and extends adds the insides of the wrapper
        que.extend(getNeighbors(root), 0)
        if (target == path):
          return True
        if (len(path) > target): #Its okay, if a valid word is found it will be there on another pass
          return False
  return False


def boggle(word, matrix):
  for i in range(0, len(matrix):
    for j in range(0, len(matrix):
      if (DFS((matrix[i][j], i, j), word)):
        return True
  return false





