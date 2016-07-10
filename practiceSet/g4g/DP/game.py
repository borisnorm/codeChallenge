#Optimal strategy for a game

'''
Problem statement: Consider a row of n coins of values v1 . . . vn, where n is even. We play a game against an opponent by alternating turns. In each turn, a player selects either the first or last coin from the row, removes it from the row permanently, and receives the value of the coin. Determine the maximum possible amount of money we can definitely win if we move first.
'''
#Recursive relationship
def game(array, hi, low):
  if low > hi:
    return 0
  else:
    return max(
      #Take into account the 4 moves that could be made, you only get one selection
      game(array, hi - 1, low + 1) + array[hi],
      game(array, hi - 1, low + 1) + array[low],
      game(array, hi - 2, low) + array[hi],
      game(array, hi, low + 2) + array[low]
    )

#DP solution
def game(array, hi, lo):
  #The memoization is here
  memo = [[0 for x in range(len(array) + 2)] for y in range(len(array) + 2)]

  for lo in range(1, len(array) + 1):
    for hi in range(1, len(array) + 1):
      #How do i factor in skipping here? - A decision at a certain left, right bound the value is that value + unlocked from the double, double lr, and split
      #The values that you get work
      memo[lo][hi] = max(
        #Is this right? my last point was 2 away or 1 away, from both sides must have plus or minus?
        memo[lo][hi+1] + array[hi],
        memo[lo][hi+2] + array[hi],
        memo[lo-1][hi] + array[lo],
        memo[lo-2][hi] + array[lo],
      )

  max_value = 0
  for i in range(len(memo)):
    for j in range(len(memo[0]):
      if memo[i][j] > max_value:
        max_value = memo[i][j]

  return max_value
