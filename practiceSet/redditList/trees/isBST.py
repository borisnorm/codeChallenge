# isBST

def isBST(root):
  if root is None:
    return True
  #vary your check case
  if (root.left.value > root.value or root.right.value =< root.value):
    return False
  else:
    return isBST(root.left) && isBST(root.right)
