#The smallest positive integer that cannot be represent as a sum of any subset
#O(n) given that it is sorted
#Find the range of subsets, accumilated sum, walk, and return non contingous

#Think of the edge cases, repeated terms, etc

def sum_rep(array):
  counter = 0
  range_array = []

  for i in array:
    range_array.append(i + counter)
    counter += i

  if range_array[0] > 2:
    return 1

  #Walk the array
  for i in range(1, len(range_array)):
    if range_array[i] - range_array[i-1] > 1:
      return range_array[i]

  return range_array(len(range_array) - 1) + 1

