#Find Max Path Sum in a binary Tree - root to leaf sum

def max_path(root):
  if root is None:
    return 0
  else:
    return max( max_path(root.left) + root.value, max_path(root.right) + root.value )


