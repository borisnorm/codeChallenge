#Find min and max depth of binary tree

def min_depth(root):
  if root is None:
    return 0
  else:
    return min(min_depth(root.left) + 1, min_depth(root.right) + 1)

def height(root):
  if root is None:
    return 0
  else:
    return max(height(root.left) + 1, height(root.right) + 1)


