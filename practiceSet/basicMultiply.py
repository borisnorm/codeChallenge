#Multiply two number without multiplcation


def mult(numOne, numTwo):
  counter  = min(numOne, numTwo)
  base = max(numOne, numTwo)
  solution = 0
  while (counter > 0):
    solution += base
    counter -= 1
  return solution













