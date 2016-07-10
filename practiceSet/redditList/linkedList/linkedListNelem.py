

def n_element(linkedList, n):
  pointer = linkedList.head
  counter = 0
  while (counter < n):
    pointer = pointer.next
  return pointer

