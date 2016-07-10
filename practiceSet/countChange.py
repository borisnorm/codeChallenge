#Given coin values of [a, b, c..], how many ways can you achieve a target value
#See if you can even hit a target in the first place

#naive, put this in a wrapper function, to return the counter
global counter = 0:
def countWays(array, target):
  if (target == 0):
    counter += 1
    return
  if (target < 0):
    return
  for i in range(0, len(array)):
    countWays(array, target - array[i])


#Overlapping sub problems, see if a hit might be different than anything else
#Hit a counter when there is a match does that also work?

#only n2 possible input spaces
def countWays(array, target):
  memo = [0 for x in range(target)]:
  for i in range(target):
    for j in range(target):
      #Two situations when i would add things up - index is the value, only once, the sum of the previous indices
      if array[j] == i:
        memo[i]++
      if (i - j) > 0:
        memo[i] += memo[i - j]
  return memo[target]

