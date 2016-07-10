#BST Serializer

#Pre Order Traversal for a BST
def tree_serialize(root, array):
  array.append(root.value)
  tree_serialize(root.left, array)
  tree_serialize(root.right, array)

def solution_wrapper(root):
  array = []
  tree_serialize(root, array)
  return array

#Post Order Traversal for a BST
  #Write a straight up add function since its sorted?
  #n log n

def insert(root, value):
  if root is None:
    newNode = new Node(value)
    return newNode
  else:
    if value > root:
      return insert(root.right, value)
    if value < root:
      return insert(root.left, value)

def createBST(array):
  root = new Node(array[0])
  for i in range(1, len(array)):
    insert(root, array[i])
  return root


#Given a pre-order traversal construct as BST
#Linear time insert if its in the correct range then just insert it

def rebuild(node, array):
  newNode = new Node(array.pop(0))

































