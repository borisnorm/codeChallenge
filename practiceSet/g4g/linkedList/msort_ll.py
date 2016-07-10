#merge sort a linked list

#Take two sorted lists and merge in linear time
def merge(llistOne, llistTwo):
  solution = list()
  pointerOne = listOne.head
  pointerTwo = listTwo.head
  while (pointerOne != None and pointerTwo != None):
    if pointerOne.value <= pointerTwo.value:
      solution.insertTail(pointerOne)
      pointerOne = pointerOne.next
    else:
      solution.insertHead(pointerTwo)
      pointerTwo = pointerTwo.next
  if (pointerOne is None):
    while (pointerTwo != None):
      solution.insertTail(pointerTwo)
      pointerTwo = pointerTwo.next

  if (pointerTwo is None)
    while (pointerOne != None)
      solution.insertTail(pointerOne)
      pointerOne = pointerOne.next
  return solution

#easier walk through list, make two and return tuple
def split_list(llist):
  length = 0
  start = llist.head
  pointer = llist.head
  while (pointer != None):
    length += 1
    pointer = pointer.next

  counter = 0
  pointer = llist.head
  solution = llist()
  while counter < length / 2:
    solution.addTail(pointer)
    pointer = pointer.next
    counter += 1
    llist.removeHead()
  return solution

#Alternate solution
counter = 0
pointer = llist.head
solutionOne = llist()

while counter < length / 2:
  solutionOne.addTail(pointer)
  pointer = pointer.next
  counter += 1

solutionTwo = llist()
while pointer != None:
  solutionTwo.addTail(pointer)
  pointer = pointer.next

return (solutionOne, solutionTwo)
#End of alternate code

def mergeSort(llist):
  if llist.length == 1:
    return llst
  else:
    #In need a helper function to split the list
    left = split_list(llist)
    right = llist #has now been mutated
    return merge(left, right)



