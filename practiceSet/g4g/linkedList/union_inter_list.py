#Union does not have to be in both
def intersection(llistOne, llistTwo):
  solution = List()
  pointer = llistOne.head
  while (pointer is not None):
    seeker = listTwo.head
    while (seeker is not None):
      if seeker.value == pointer.value:
        newNode = Node(seeker.value)
        solution.insert(newNode)
      seeker = seeker.next
  return solution

#With extra memory
#Walk through both lists and store in seprate sets
#Walk through one list, if its in the other set, then add to soln

def union(llistOne, llistTwo):
  present = Set()
  pointerOne = listOne.head
  pointerTwo = listTwo.head
  while (pointerOne != None):
    if pointerOne.value not in present:
      present.add(pointerOne.value)
    pointerOne = pointerOne.next

  while (pointerTwo != None):
    if pointerTwo.value not in present:
      present.add(pointerTwo.value)
    pointerTwo = pointerTwo.next

  solution = llist()
  for item in present:
    solution.insert(item)

  return solution

