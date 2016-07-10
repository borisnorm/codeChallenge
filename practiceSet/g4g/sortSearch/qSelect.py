#Find the kth element in an unsorted array

def partition(array, i, j):
  hi = j
  lo = i + 1
  pivot = array[i]
  while True:

    while (array[lo] < pivot):
      lo += 1

    while (array[hi] > pivot):
      hi -= 1

    if lo > hi:
      array[lo], array[hi] = array[hi], array[lo]
      return hi

    array[lo], array[hi] = array[hi], array[lo]
    lo += 1
    hi -= 1

def qSelect(array, k, lo, hi):
  index = parition(array, lo, hi)
  if index == k:
    return array[k]
  if k > index:
    return qSelect(array, k - index, index + 1, hi)
   #if k < index:
  else:
    return qSelect(array, k, low, index - 1)

#Initalize the solution with the proper components


