#check if a bt is a subtree of another bt
def equal(root1, root2):
  if root1.value == root2.value:
    return True
  if root1.value != root2.value:
    return False
  else:
    return equal(root1.left, root2.left) && equal(root1.right, root2.right)

def serialize(root, array):
  if root is None:
    array.append('*')
  else:
    array.append(root.value)
    serialize(root.left, array)
    serialize(root.right, array)

def subtree_check(root, subtree_root):
  if root is None and subtree_root is None:
    return True
  if root is None:
    return False
  if root == subtree_root:
    return equal(root, subtree_root)
  else:
    return subtree_check(root.left, subtree_root) or subtree_check(root.right, subtree_root)

  #Out dated checker funciton
  '''
  if root == subtree_root:
    candidate = []
    subtree = []
    serialize(root, candidate)
    serialize(subtree_root, subtree)
    if len(candidate) != len(subtree):
      return False
    for i in range(len(candidate)):
      if candidate[i] != subtree[i]:
        return False
    return True
  '''
