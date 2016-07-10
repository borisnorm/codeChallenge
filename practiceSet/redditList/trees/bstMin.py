#Smallest element in a BST

def min_bst(root):
  if root.left is None:
    return root.value
  else:
    return min_bst(root.left)


