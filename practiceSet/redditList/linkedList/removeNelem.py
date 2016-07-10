def remove_n_elem(linkedList, n)):
  pointer = linkedList.head
  counter = 0
  while (counter < n):
    if counter == n:
      pointer.prev.next = pointer.next
      pointer.next.prev = pointer.prev
      pointer.next = None
      pointer.prev = None
      return pointer.value
  return False


