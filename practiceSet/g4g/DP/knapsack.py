#The Knapsack Problem
'''
Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum total value in the knapsack.
'''

#Recursive knap sack, you choose it or not
def kp(array, run_sum, weight):
  if run_sum > weight:
    return
  if len(array) == 0:
    return run_sum
  else:
    return max(
      #Choose if you want this or not
      kp(array[1:], run_sum += array[0], weight),
      kp(array[1:], run_sum, weight)
    )

#DP knapsack
#Sorted stuff is ideal
def kp(array, weight):
  memo = [[0 for x in range(len(array) + 1)] for y in range(len(array) + 1)]
  for i in range(1, len(array) + 1):
    for j in range(1, len(weight) + 1):
      if array[i] < j and memo[i-1][j] + array[i] <= weight:
        if memo[i-1] < weight]:
          memo[i][j] = max(
            memo[i-1][j],
            #why is this extra j parameter here?
              #lookback before you had the weight and then add it
            memo[i-1][weight - array[i-1]] + array[i-1]
          )
  return memo[i][j]


        memo[i][j] = max(
          #If choose to add, value or not, lets say you had the max value for all of the things previously, the solution is just a test
          memo[i-1][j],
          memo[i-1][j] + array[i]
        )
  return memo[i][j]

