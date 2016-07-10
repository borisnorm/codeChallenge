#Print a tree by levels
#One way to approach this is to bfs the tree

def tree_bfs(root):
  queOne = [root]
  queTwo = []
  #i need some type of switching mechanism
  while (queOne or queTwo):
    print queOne
    while(queOne):
      item = queOne.pop()
      if (item.left is not None):
        queTwo.append(item.left)
      if (item.right is not None):
        queTwo.append(item.right)

    print queTwo
    while(queTwo):
      item = queTwo.pop()
      if (item.left is not None):
        queOne.append(item.left)
      if (item.right is not None):
        queOne.append(item.right)

