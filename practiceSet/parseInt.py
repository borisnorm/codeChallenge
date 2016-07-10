#Convert a number in one base to a number of anothe base

def parse_int(number, oldBase, newBase):
  #Convert this number to base 10
  solution = 0
  num = str(number)
  counter = len(str(number))
  for i in range(0 , counter):
    solution = solution + num[i] * pow(oldBase, counter)
    counter -= 1

  #Then convert this number to another base
  newNumber = []
  while (solution > 0):
    newNumber.insert(solution % newBase, 0)
    solution = solution / newBase
  return ''.join(map(str, newNumber))














