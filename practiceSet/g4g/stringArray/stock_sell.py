#Buy and Sell Stock to max profits

#Once
def stock_profit(array):
  min_val = 10000
  max_val = 0
  profit = 0
  for i in array:
    if i < min_val:
      min_val = i
    if i - min_val > profit:
      profit = i - min_val
  return profit

'''
Given an array of stock values , where ith element is the value of stock at the ith day.
 Find the maximum money you can earn by buying and selling stocks, given that you can buy/sell only one stock at a particular day, (However you can have multiple stocks with you at any point of time) .
'''
def profit(array, stocks):
  if len(array) == 0:
    return 0
  else:
    return max(
      profit(array[1:], stocks),
      profit(array[1:], stocks + 1) - array[0]),
      profit(array[1:], stocks - 1) + array[0])
    )

def profit(array, stocks):
  memo = [[0 for x in range(k)] for y in range(len(array))]
  for i in range(len(array)):
    for j in range(stocks):
      #Do i need to pad things here? for i and j?
      memo[i][j] = max(
        memo[i - 1][j],
        memo[i - 1][j - 1] - array[i],
        memo[i - 1][j + 1] + array[i]
      )




