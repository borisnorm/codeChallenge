#Binary search on a rotated array, no repeates
#extra challenge in the first term [5, 6, 7, 8, 1, 2, 3, 4]
#repeated array modification time
#always pre-write method signatures, before you solve the problem

def find_pivot(array, low, hi):
  if lo >= hi:
    return -1

  mid = hi + lo / 2
  if array[mid + 1] < array[mid]:
    return mid

  #The pivot must be between these ranges (low mid and high mid are the only changes)
  if array[mid] < array[low]:
    return find_pivot(array, low, mid)

  if arrary[hi] < array[mid]:
    return find_pivot(array, low, mid)

  #Else it is between another range
  if array[low] < array[mid]:
    return find_pivot(array, mid, hi)

  if array[hi] > array[mid]:
    return find_pivot(array, low, mid)

#Then return binary search on each side of the pivots to get the answer


#How to modify this for duplicate elements?




