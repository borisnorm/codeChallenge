#Given a tree verify a tree contains a subtree

#Traversal print method
def compareTraversal(arrayOne, arrayTwo):
  for i in range(arrayOne):
    #I might need to catch some error exception
    if (arrayOne[i] == arrayTwo[i]):
      return False
    return True

#Wrapper function for traversal helper
def traversal(root):
  array = []
  traversal_helper(root, array)
  #VIA COLSURES, and a stack of them one return value does not kill everything
  return array

def traversal_helper(root, array):
  if (root is None):
    return
  else:
    array.append(root)
    traversal_helper(root.left, array)
    traversal_helper(root.right, array)

#The key thing is how do you know, to return the array when it is all done - BASED ON CLOSURES
def subTreeCheck(rootOne, subTreeTraversal):
  if (rootOne is None):
    return
  if (rootOne.value == subTreeTraversal[0]):
    rootTraversal = traversal(rootOne):
    if compareTraversal(rootTraversal, subTreeTraversal)
      return True

#Still not, done yet how do I get this to yield false
def subTreeWrapper(rootOne, rootTwo):
  subTreeTraversal = traversal(rooTwo):
    return subTreeCheck(rootOne, subTreeTraversal)


#Check if Two Trees are equal, true and false take adv of the logic manipulation
def equalTree(root1, root2):
  if (root1 is None and root2 is None):
    return True
  if (root1 && roo2):
    return (root1 == root2) && equalTree(root1.left, root2.left) && equalTree(root1.right, root2.right)
  #It should return false in the case, there off, false is already returnd
  return False:
















