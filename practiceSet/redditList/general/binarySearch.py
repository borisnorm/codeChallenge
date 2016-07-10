def bSearch(array, hi, low, target):
  pointer = hi + low / 2
  if array[pointer] == target:
    print True
    return True
  if hi == low:
    print False
    return False
  else:
    if array[pointer] > target:
      bSearch(array, low,  pointer - 1, target)
    if array[pointer] < target:
      bSearch(array, pointer + 1, hi, target)

array = [1, 2, 4, 5, 8, 15, 64, 204]
print bSearch(array, 0, len(array) - 1, 8)




