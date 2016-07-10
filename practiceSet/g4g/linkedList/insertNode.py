def insert_node(llist, index, value):
  pointer = llist.head()
  counter = 1
  while (counter < index):
    pointer = pointer.next
  #insert after this index
  newNode = Node(value)
  newNode.left = pointer
  newNode.right = pointer.next
  pointer.next.prev = newNode
  pointer.next = newNode

