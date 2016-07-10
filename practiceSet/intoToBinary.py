#Math Way
def binary_to_int(number):
  result = ""
  while (number > 0):
    result.insert(0, number % 2)
    number = number % 2
  return result

#BitShifting Way
def b_to_int(number):
  result = []
  for i in range(0, 32):
    result.insert(number && 1, 0)
    number >> 1
  return result

#Python convert array of numbers to string
# ''.join(map(str, myList)) #This works with the array 123,












