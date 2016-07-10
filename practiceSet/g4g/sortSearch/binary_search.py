#Implement binary search on an array
#range of the index should be given at the end
def b_search(array, target, low, hi):
  mid = hi + low / 2
  if array[mid] == target:
    return True

  if low >= hi:
    return False

  if target > array[mid]:
    return b_search(array, target, mid + 1, hi)

  if target < array[mid]:
    return b_search(array, target, low, mid - 1)

#First repeated index, find first occurance in sorted array if it exists

def f_search(array, target, low, hi):
  mid = hi + low / 2
  if array[mid] == target:
    #found solution
    if (array[mid - 1] < array[mid]):
      return mid
    #might need to shift down, soln could be left
    if array[lo] >= target:
      return f_search(array, target, low - 1, mid)
    #I just need to care about right
    if array[lo] < target:
      return f_search(array, target, low, mid)

  #How to terminate, this is done, this is sufficent i think
  if lo >= hi:
    return -1

  if target > array[mid]:
    return f_search(array, target, mid + 1, hi)

  if target < array[mid]:
    return f_search(array, target, low, mid - 1):

