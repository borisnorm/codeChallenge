#Find the LCA in a BT and a BST

#BT Search
def search_path(root, target, path):
  if root is None:
    return False
  path.append(root)
  if (root.value == target.value):
    return True
  else:
    #Search will just not be initalized if null
    if (root.right && search_path(root.right, target, path)) or (root.left && search_path(root.left, target, path)):
      return True

    #Pop this out
    path.pop()
    return False

#Must traverse who length, you dont know if it will be in synch
def find_lca(root, nodeOne, nodeTwo):
  arrayOne = []
  arrayTwo = []
  #Initalize search as the check case at the same time
  if (search_path(root, nodeOne, arrayOne) && (search_path(root, nodeONe, arrayOne)):
      return - 1

  #Just have one counter and the larger one will prevail
  counter = 0
  while (counter < len(arrayOne) or counter < len(arrayTwo)):
    if arrayOne[counter] != arrayTwo[counter]:
      return arrayOne[counter - 1]
    counter += 1


#BT Search the Smart Way, without extra memory
  #If n1 or n2 match with the root, the root is LCA (assume both present how to check?)
    #I assume that some type of search must happen on the subtree
    #This works because find LCA now becomes a new type of search
def lca(root, nodeOne, nodeTwo):
  if root is None:
    return None
    #If The first one returned must be the LCA (how to check its in subtree?)
    #if you encouter a hit first it must be at the root
    if (root.vaue == nodeOne.value) or (root.value == nodeTwo.value):
      return root
    left_lca = lca(root.left, nodeOne, nodeTwo):
    right_lca = lca(root.right, nodeOne, nodeTwo):
    #this is the brilliant check that makes sure that it is in the subtree
    if left_lca and right_lca:
      return root
    if left_lca is not None:
      return left_lca
    else:
      return right_lca


#BST
def lca_bst(root, node1, node2):
  #This assumes that those nodes are the upper and lower bound
  if root is None:
    return None
  #equality check is already handled at this location
  if node1 <= root.value <= node2:
    return root
  #check if its greater or less than both nodes, i assumed they were in bounds
  if root < node1 and root < node2
    lca_bst(root.right, node1, node2)
  if root > node2 and root > node1
    lca_bst(root.left, node1, node2)


#Parent Pointers, traverse equal heights without storage

#Search height might be different
def search_height(root, target, height):
  if root is None:
    return -1
  if root is target:
    return height
  else:
    #either you return -1, or a correct search height
    return max(search_height(root.left, target, height + 1), search_height(root.right, target, height + 1))

def lca_parent(root, node1, node2):
  node1_h = search_height(root, node1, 0)
  node2_h = search_height(root, node2, 0)
  if node1_h > node2_h:
    counter = node1_h - node2_h
    while (counter > 0):
      node1 = node1.parent
      counter -= 1

  if node2_h > node1_h:
    counter = node1_h - node2_h
    while (counter > 0):
      node2 - node2.parent
      counter -= 1

  while (node1 != node2):
    node1 = node1.parent
    node2 = node2.parent

  return node1

