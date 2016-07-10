def isPal(string):
  if string = string[::-1]
    return True
  return False

def isPal(array):
  lo = 0
  hi = len(array) - 1
  while lo < hi:
    if array[lo] != array[hi]):
      return False
  return True

def arrayElmIsPal(array):
  for i in range(len(array)):
    if isPal(array[i]) is False:
      return False
  return True

def partition(string)
  array = string.split()
  solution = []
  return solution

def parted(array, current, final, solution):
  if len(array) == 0:
    if len(current) == 0:
      solution.append(final)
    if len(current) > 0:
      #This is because mandatory brackets
      if arrayElemIsPal([current] + final):
        solution.append([current] + final)
    else:
      parted(array[:1], current + array[0], final)
      parted(array[:1], current, final + [[array[0]])


