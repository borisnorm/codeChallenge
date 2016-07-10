#Find the Comon Elements of Two arrays
  #Just the unique common character
  #Just list the repeated common characters

#If not sorted
#Hash one of the arrays, iterate through than the search, linear time
#linear time complexity

def common_elements(arrayOne, arrayTwo):
  itemSet = set()
  solution = []
  for i in range(arrayOne):
    itemSet.add(arrayOne[i])
  for j in range(arrayTwo):
    if arrayTwo[j] is in itemSet:
      solution.append(arrayTwo[j])
  return solution

def removeDuplicates(array):
  solution = []
  seenBefore = set()
  for i in range(array):
    if array[i] not in seenBefore:
      solution.append(array[i])
      seenBefore.add(array[i])
  return solution


