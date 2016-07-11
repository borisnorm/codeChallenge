#Given two nodes in a tree, return the LCA of the tree
#given a pointer

class Solution:

    #Tree and 2 nodes are given
    def height(node):
        if node is None:
            return 0
        else:
            return max(height(node.left) + 1, height(node.right) + 1)

    def adjusted_node(node, up_steps):
        counter = 0
        pointer = node
        while counter < up_steps:
            pointer = node.parent
        return pointer

    def level_lca(root, node1, node2):
        pointer1 = node1
        pointer2 = node2
        while pointer1 != pointer2:
            pointer1 = pointer1.parent
            pointer2 = pointer2.parent
        return pointer1

    def lca(root, node1, node2):
        nodeHeightOne = height(node1)
        nodeHeigthTwo = height(node2)
        diff = abs(nodeHeightOne - nodeHeightTwo)

        if nodeHeightOne > nodeHeightTwo:
            adjusted_node1 = adjusted_node(node1, diff)
            return level_lca(root, adjusted_node1, node2)

        if nodeHeightOne < nodeHeigtTwo:
            adjusted_node2 = adjusted_node(node2, diff)
            return level_lca(root, node1, adjusted_node2)
