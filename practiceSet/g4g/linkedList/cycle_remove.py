#Remove cycle in linkedlist

def remove_cycle(llist):
  s = set()
  pointer = llist.head
  pointer_lead = llist.head.next
  while pointer_lead is not None:
    if pointer_lead is in s:
      #cycle found - remove it
      pointer.next = None
      return llist
    s.add(pointer_lead)
    pointer_lead = pointer_lead.next
    pointer = pointer.next
  return llist

#Either way non cycle

