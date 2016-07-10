#Binary Search on a Rotated Array
#Find the pivot point on a rotated array with slight modificaitons to binary search
#There is reason why the pivoting does not phase many people
#[5, 6, 7, 8, 1, 2, 3, 4]

def find_pivot_index(array, low, hi):
  #DONT FORGET THE BASE CASE
  if hi < low:
    return 0
  if hi == low:
    return low

  mid = (low + hi) / 2

  #pivot turns when, mid and mid - 1 work
  #If indicies are correct, and pivot starts at mid
  if (mid < hi && arr[mid] > array[mid + 1]):
    return mid
  #hi low are correct, and pivot starts ad mide -1
  if (mid > low && arr[mid] < array[mid - 1]):
    return mid - 1

  #two other check cases which are key
  #if lower is greater than mid pivot, the pivot is between them
  if array[low] >= array[mid]:
    #why is it mid - 1?
    return find_pivot_index(array, low, mid - 1):
  #if array[low] < array[mid]: if hi is greater than mid, pivot is not here
  else:
    #If it is not between them, they must be somewhere else
    #slowly incremenet this thing by 1?
    return find_pivot_index(array, mid + 1, hi)



