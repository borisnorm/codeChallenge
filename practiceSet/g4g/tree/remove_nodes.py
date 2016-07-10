#remove nodes on root leaf paths of length < k
#tree pruning, if the max height of the subtree is less than k then remove?
#naive, for every node if left or right subtree max len from root is < k, then it is none
def length(root):
  if root is None:
    return 0
  else:
    return max(length(root.left) + 1, length(root.right) + 1)

#default arg should be 0
def remove_nodes(root, distance, k):
  if root is None:
    return
  if length(root.left) + distance < k:
    return root.left = None
  if length(root.right) + distance < k:
    return root.right = None
  else:
    remove_nodes(root.left, distance + 1, k)
    remove_nodes(root.right, distance + 1, k)













