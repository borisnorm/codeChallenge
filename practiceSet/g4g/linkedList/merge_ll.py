#merge linked lists at alternate positions

def pop_head(llist)
  head = llist.head
  head.next.prev = None
  head.prev.next = head.next
  head.next = None
  head.prev = None
  llist.size -= 1
  return head

def merge(llistOne, llistTwo):
  #merge list two into listOne
  pointer = listOne.head
  while llistTwo :
    #check for smallerListone
    if pointer.next is None:
      pointer.next = llistTwo.head
      llistTwo.prev = pointer
    #Pop and then add it in
    node = pop_head(llistTwo)
    node.prev = pointer
    node.next = pointer.next
    pointer.next.prev = node
    pointer.next = node
    pointer = pointer.next.next
  return llistOne
















