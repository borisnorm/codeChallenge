#Check if tree is sum tree in constant time
def isLeaf(root):
  if (root.left is None && root.right is None):
    return True
  return False


def sumCheck(root):
  if root is None:
    return True
  if isLeaf(root):
    return True
  if (isLeaf(root.left) && !isLeaf(root.right)) or (isLeaf(root.right) && (isLeaf(root.left))):
    return False
  if (sumCheck(root.left) && sumCheck(root.right)):
    #find left Sum
    ls = None
    if (root.left is None):
      ls =  0
    if isLeaf(root.left):
      ls = root.left.value
    else:
      ls = 2*root.left.value

    #find right Sum
    rs = None
    if (root.right is None):
      rs = 0
    if isLeaf(root.right):
      rs = root.right.value
    else:
      rs = 2*root.right.value

    #Compare the two then return
    if (root.value = ls + rs):
      return True
    else:
      return False

  else:
    return False




