#Distance between two nodes in a BST and a BT

#Search in a Binary Tree
def distance_bst(root, target, height):
  if root is None:
    return -1
  if (root == target):
    return height
  else:
    return max(distance_bst(root.left, target, height + 1), distance_bst(root.right, target, height + 1))

#Search in a BST
def distance_bt(root, target, height):
  if root is None:
    return -1
  if (root == target):
    return height
  else:
    if root.value >= target.value:
      return distance_bt(root.left, target, height + 1)
    return distance_bt(root.right, target, height + 1)

#BT Path - else, runs an if statement
#To delete this every time
def bt_path(root, target, path):
  path.append(root)
  if root.value == target.value:
    return True
  if (root is None):
    return False
  if (!bt_path(root.left) or !bt_path(root.right)):
    path.pop(root)

#BST LCA
def bst_lca(root, node1, node2):
  node1 = min(node1, node2)
  node2 = max(node1, node2)
  if (root is None):
    return False
  if node1.value <= root.value <= node2.value:
    return root
  if root.value < node1.value:
    return lca(root.left, node1, node2
  else:
    return lca(root.right, node1, node2)

#BT LCA - array, pop path - Something is wrong if i need path
def bt_lca(root, node1, node2, path):
  #This does assume the other thing is in the graph
  if (root is node1) or (noot is node2):
    return True
  if (root is None):
    return False
  else:
    return bt_lca(root.right) && bt_lca(root.left)

#Distance is distance1 + distance2 - 2 * lca





