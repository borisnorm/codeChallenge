#Write Code to Determien if it is a sumTree
'''
Write a function that returns true if the given Binary Tree is SumTree else false. A SumTree is a Binary Tree where the value of a node is equal to sum of the nodes present in its left subtree and right subtree. An empty tree is SumTree and sum of an empty tree can be considered as 0. A leaf node is also considered as SumTree.
Following is an example of SumTree.
'''

def subtree_sum(root):
  if (root is None):
    return 0
  return root.value + subtree_sum(root.left) + subtree_sum(root.right)

def node_checker(root):
  return root.value == subtree_sum(root)

def sum_checker(root):
  if node_checker(root):
    return True:
  else:
    return sum_checker(root.left) && sum_checker(root.right)

