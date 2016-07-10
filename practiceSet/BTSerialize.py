#Serialize and deserialize a Binary Tree

def writeBT(root, array):
  if root is None:
    array.append('#')
  else:
    array.append(root.value)
    writeBT(root.left, array)
    writeBT(root.right, array)


#De-serialize the Tree, follow the traversal
def nextToken(array):
  return array.pop(0) #pop the front


def readBT(root, array, pointer):
  if array[0] == '#':
    return None
  else:
    #They have a function to read from a tree, but this is different
    root.value = array[pointer]
    readBT(root.left, array, pointer + 1)
    readBT(root.right, array, pointer + 2)

#They have a read token implemention, something else to work with
def readBT(node, stream):
  token = 0
  isNumber = false
  if (!readNextToken(token, isNumber, stream):
    return
  if (isNumber):
    neNode = new Node(token)
    readBT(node.left, stream)
    readyBT(node.right, stream)

def readNextToken(token, isNumber, stream):
  item = stream.pop(0)
  if type(item) is 'integer':
    isNumber = True
    token = item
    return True
  return False

