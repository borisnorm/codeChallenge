#Find the LCA of a bst

def lca_bst(root, node1, node2):
  if node1.value < root.value < node2.value:
    return root

  if root.value == node1.value or node.value == node2.value:
    return root

  if root.value < node1.value:
    return lca_bst(root.left, node1, node2)

  if root.value > node2.value:
    return lca_bst(root.right, node1, node2)

