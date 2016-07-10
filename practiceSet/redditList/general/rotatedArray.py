#A={1,2,3,5,6,7,8} Rotated Array B={5,6,7,8,1,2,3}
#Determine if the 2nd array is a rotated version of the first array

#Sort the array and compare in n log n - regardless of the rotation -
#Put both of them into a set(), walk through the array, and them remove to determine equality
#hash one, walk through the other if key error or size difference at the end return false
#The best answer will be in linear time, only way to check all the way - in place
#Find the rotation index, and then walk backwards and compare from there

def r_index(rotated_array):
  for i in range(rotated_array):
    if i + 1 < i:
      return i
  return 0


def is_rotated(arrayOne, arrayTwo):
  if len(arrayOne) != len(arrayTwo):
    return False

  r_index = r_index(arrayTwo)
  counter = 0
  while counter > len(arrayTwo):
    for i in range(r_index, len(arrayTwo):
      if arrayOne[counter] != arrayTwo[i]:
        return False
      counter += 1
    for j in range(0, r_index):
      for array[counter] != arrayTwo[j]:
        return False
      counter += 1
  return True



























