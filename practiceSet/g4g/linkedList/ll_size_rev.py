#Reverse a list in groups of a given size
#Reversing sublists of a given size

def reverse(llist, startNode, endNode):
  low = startNode
  hi = endNode
  while low != hi:
    temp = low.value
    low.value = hi.value
    hi.value = temp
    low = low.next
    hi = hi.prev
  return

#End no hookup because value swap
def size_rev(llist, k):
  startPointer = llist.head
  pointer = llist.head
  counter = 0
  while True:
    while counter < k
      if pointer is None:
        return llist
      pointer = pointer.next
      counter += 1
    reverse(llist, startPointer, pointer)
    startPointer = pointer.next
    pointer = pointer.next
    counter = 0
  return llist










