#Can a given array represent a pre-order traversal of a tree

def can_represent(array, root):
  pre_order_serialized = []
  pre_serialize(root, pre_order_serialized)
  if len(array) != len(pre_order_serialized):
    return False
  for i in range(len(array)):
    if pre_order_serialized[i] != array[i]:
      return False
  return True

def pre_serialize(root, array):
  if root is None:
    array.append('*')
  else:
    array.append(root.value)
    pre_serialize(root.left, array)
    pre_serialize(root.right, array)

