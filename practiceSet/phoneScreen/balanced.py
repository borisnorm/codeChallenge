#For every node, left and rightt subtrees differ by no more than 1

class Solution:

    #For each node, check the heights that is n squared
    #Find the difference, between max and min height in both subtree
        #I dont think that works because height implies max

    def height(root):
        if root is None:
            return 0
        else:
            return max(height(root.left), height(root.right))

    #Find a better way to deal with this one
    def isBalanced(root):
        if root is None:
            return True
        if abs(height(root.left - root.right):
            return isBalanced(root.left) and isBalanced(root.right)
        return False

