#Does a linked list have cycles

def cycleCheck(linkedList):
  slowPointer = linkedList.head
  fastPointer = linkedList.head.next
  while (slowPointer && fastPointer):
    if (slowPointer is fastPointer):
      return True
    slowPointer = slowPointer.next
    fastPointer = fastPointer.next
  return False

