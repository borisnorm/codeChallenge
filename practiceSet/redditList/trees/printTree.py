#Print Tree using BFS and DFS

def dfs_print(root):
  if root is None:
    return
  else:
    #shift print down, for pre, in, or post order
    print root.value
    dfs_print(root.left)
    dfs_print(root.right)

def bfs_print(root):
  queOne = [root]
  queTwo = []
  while (queOne && queTwo):
    print queOne
    while (queOne):
      item = queOne.pop(0)
      if (item.left):
        queTwo.append(item.left)
      if (item.right)
        queTwo.append(item.right)

    print queTwo
    while (queTwo):
      item = queTwo.pop(0)
      if (item.left):
        queOne.append(item.left)
      if (item.right):
        queTwo.append(item.right)











