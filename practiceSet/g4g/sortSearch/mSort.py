#merge Sort
def merge(array1, array2):
  solution = []
  #This should be an or not an and
  while (array1 or array2):
    if len(array2) == 0 or array1[0] <= array2[0]:
      if array1:
        solution.append(array1.pop(0))
      #this was array 2 not array1
    if len(array1) == 0 or array2[0] < array1[0]:
      if (array2):
        solution.append(array2.pop(0))
  print solution
  return solution

def mSort(array):
  print array
  if len(array) == 1:
    return array
  else:
    mid = len(array) / 2
    print mid
    #the index errors because the right is processed is why
    left = mSort(array[:mid])
    right = mSort(array[mid:])
    return merge(left, right)

test = [5, 7, 1, 32, 2, 5, 7, 100, 452, 342]
print mSort(test)

