#BST vs Regualr Tree

#BST Version
def twoNodeDist(root, node1, node2):
  #Two diff subtress, or in the subtree, return the max of all of the three cases
  return max(nodeDistance(node1, node2, 0), nodeDistance(node2, node1, 0), nodeDistance(root, node1, 0) + nodeDistance(root, node2, 0);

def nodeDistance(root, node, distance):
  if (root is None):
    return 0
  if (root === node):
    return distance
  if (root > node):
    return nodeDistance(root.left, node, distance + 1)
  return nodeDistance(root.right, node, distance + 1)

#Regular Tree Version, the difference is nodeDistance
def nodeDistance(root, node, distance):
  if (root is None):
    return 0
  if (root === node):
    return distance
  return max(nodeDistance(root.left, node, distance + 1), nodeDistance(root.right, node, distance + 1))
























