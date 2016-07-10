#Check if a linked list a palindrome

#SLIST - This will be n2 time



#DLSIS
def pal_check(dlist):
  frontCounter = 0
  endCounter = dlist.size - 1
  front = dlist.head
  end = dlist.tail
  while (frontCounter < endCounter):
    if (frontCounter.value != endCounter.value):
      return False
    else:
      frontCounter += 1
      endCounter -= 1
      front = front.next
      end = end.prev
  return False

