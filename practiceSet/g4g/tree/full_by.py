#Check if a binary tree is full or not
'''
A full binary tree (sometimes proper binary tree or 2-tree) is a tree in which every node other than the leaves has two children. A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled, and all nodes are as far left as possible.
'''
#Recursion
def full_check(root):
  if root is None:
    return True
  #might change the order but its still correct i think
  if (root.left) && (root.right):
    return full_check(root.left) && full_check(root.right)
  return False

#Level order traversal, find the height, iteratively check the proper tree count
#Recusively find make sure the min heights are within 1 of each other, and the tree is full
#Checking full might be doable if you know the min_height, at that height ignore the rules

def min_height(root):
  if root is None:
    return 0
  else:
    return min(min_height(root.left) + 1, min_height(root.right) + 1)

def full_check(root, height, last_level):
  if root is None:
    return True
  if ((root.right) && root.left is None) or ((root.left) && root.right is None) && height < last_level):
    return False
  return full_check(root.left, height + 1, last_level) && full_check(root.right, height + 1, last_level)

#DONT NEED THIS
def complete_check(root):
  left_min = min_height(root.left)
  right_min = min_height(root.right)
  if abs(left_min - right_min) > 1:
    return False
  if full_check(root, 0, mins(left_min, right_min)):
    return True
  return False


