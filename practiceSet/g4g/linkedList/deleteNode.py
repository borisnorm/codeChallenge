def delete_node(llist, value):
  pointer = llist.head
  while (pointer != None):
    if pointer == value:
      pointer.prev.next = pointer.next
      pointer.next.prev = pointer.prev
      pointer.next = None
      pointer.prev = None
      return pointer
  return None
