#Given a cycled linked list, find the node at the beginning of the loop

def beginLoop(linkedList):
  visited = set()
  pointer = linkedList.head
  while True:
    if pointer in viisted:
      return pointer
    pointer = pointer.next

