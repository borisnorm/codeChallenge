#Given a set of non-negative integers, and a value sum, determine if there is a subset of the given set with sum equal to given sum.

#Recursive solution
def sub_sum(array, sub_sum, target):
  if len(array) == 0 and (sub_sum == target):
    return True
  if len(array) == 0 and (sub_sum != target):
    return False
  return sub(array[1:], sub_sum += array[0], target) or sub(array[1:], sub_sum, target)

#Assume the array is in sorted order
#DP Solution - Store sub_sum values somewhere, there are more than n_squared, but pairwise interactions are n^2
def sub_sum(array, target):
  memo = [ [0 for x in range(len(array) + 1)] for y in range(target + 1)]

  #Pre-initialize
  for y in range(len(array)):
    memo[0][y] = True
  for x in range(len(target)):
    memo[x][0] = False
  memo[0][0] = True

  #The range here is very wrong
  for i in range(len(target)):
    for j in range(len(array)):
      #on the path to the target sum up include or not include
      #check if its greater then for problems

      memo[i][j] = memo[i-1][j] #include the old value

      if memo[i][j] == False:
        memo[i][j] = memo[i-1][j - array[i - 1]] #Try the new value out

  return memo[i][j]

