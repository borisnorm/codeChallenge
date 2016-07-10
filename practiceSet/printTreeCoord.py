#Recurrsion is hard because of the terminating case,
#What about the, BFS using 2 queues to print the level tree


coords = [];
def printTreeCoord(root, xCord, yCord, coords):
  #The hard this is how to terminate all when they are null
  #This is the trick for this case
  if (root is None)
    return
    #Not sure how to solve this
  coords.append((root.value, xCord, yCord))
  printTreeCoord(root.left, xCord - 1, yCord - 1)
  printTreeCoord(root.right, xCord + 1, yCord + 1)

 print printTreeCoord(root, 0, 0, coords)

