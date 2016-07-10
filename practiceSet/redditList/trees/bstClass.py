class Node:

  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class BST:

  def __init__(self, value):
    self.root = Node(value)
    self.size = 1

  def find_max(self, root):
    if root.right is None:
      return root
    find_max(root.right)
  def find_min(self, root):
    if root.left is None:
      return root

  def insert(self, value)
    insert_helper(self.root, value)

  def delete(self, root)
    delete_helper(self.root, value)

  #Not sure if this is 100% correct or not
  def insert_helper(self, root, value):
    if root is None:
      return Node(value)
    if value >= root.value:
      return root.right = insert_helper(root.right, value)
    else:
      return root.left = insert_helper(root.left, value)

  #This is also tricky here
  def delete_helper(self, root, target):
    if (root is target):
      if (root.left && root.right):
        leftMax = find_max(root.left)
        rightMin = find_max(root.right)
        leftMax = root.right.left

        return root.right

      #Two case is the hardest case, need to swap around
        #right child, goes to deleted place, hook up the children
        #right childs left child, get stuck to right most child of the deleted left childs sub tree
      if (root.left && root.right):
        #If root.value = value:

      if (root.left || root.right):
        if (root.left):
          return root.left
        return root.right

      if (root.left is None and root.right is None):
        return None

