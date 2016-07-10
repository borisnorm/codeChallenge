#Return a ll rep of those numbers?
def addLL_num(llOne, llTwo):
  solution = llist()
  pointerOne = llOne.tail
  pointerTwo = llTwo.tail
  carry_left = 0
  power = 1
  while (pointerOne is not None and pointerTwo is not None):
    sum_holder = carry_left + pointerOne.value + pointerTwo.value
    newNode = Node(sum_holder) % 10)
    carry_left = sum_holder - (sum_holder % 10) / power
    solution.addHead(newNode)
    pointerOne = pointerOne.prev
    pointerTwo = pointerTwo.prev
  #Add the rest of the values
  if (pointerOne is None):
    while (pointerTwo is not None):
      solution.addHead(pointerTwo)
      pointerTwo = pointerTwo.prev
  if (pointerTwo is None)
    while (pointerOne is not None):
      solution.addHead(pointerOne)
      pointerOne = pointerOne.prev
  return solution







