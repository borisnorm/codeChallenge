#Find Second largest number in a BST

#Must be the parent of the largest number, logn time
def secondLargest(root):
  if root.right.right is None:
    return root.right.value
  else:
    return secondLargest(root.right):


#Find The K largest number in a BST

#Initalize counter to 1, could put it into an array, but wastes space
def k_largest(root, counter, k):
  if root is None:
    return
  else:
    k_largest(root.left, counter + 1, k)
    #THE Location must be here not above or it will print pre, order after every hit
    if (counter == k):
      return root.value
    k_largest(root.right, counter + 1, k)











