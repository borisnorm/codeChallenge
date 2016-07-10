#Find the longest path in a matrix
#Given a n*n matrix where numbers all numbers are distinct and are distributed from range 1 to n2,
# find the maximum length path (starting from any cell) such that all cells along the path are increasing order with a difference of 1.
#We can move in 4 directions from a given cell (i, j), i.e., we can move to (i+1, j) or (i, j+1) or (i-1, j) or (i, j-1) with the condition that the adjacen

'''
Given a cost matrix cost[][] and a position (m, n) in cost[][], write a function that returns cost of minimum cost path to reach (m, n) from (0, 0). Each cell of the matrix represents a cost to traverse through that cell. Total cost of a path to reach (m, n) is sum of all the costs on that path (including both source and destination). You can only traverse down, right and diagonally lower cells from a given cell, i.e., from a given cell (i, j), cells (i+1, j), (i, j+1) and (i+1, j+1) can be traversed. You may assume that all costs are positive integers.
'''

#Longest path recusrive
def l_path(matrix):
  longest_path = 0
  for i in range(len(matrix)):
    for j in range(len(matrix)):
      length = path_finder(i, j, matrix)
      if length > longest_path:
        longest_path = length
  return longest_path

def path_finder(x, y, matrix):
  current_value = matrix[x][y]
  if x < 0 or x > len(matrix) - 1 or y < 0 or y > len(matrix) - 1:
    return 0
  if matrix[x+1][y] - current_value = 1:
    return path_finder(x+1, y) + 1
  elif matrix[x-1][y] - current_value = 1:
    return path_finder(x-1, y) + 1
  elif matrix[x][y+1] - current_value = 1:
    return path_finer(x, y + 1)
  elif matrix[x][y-1] - current_value = 1:
    return path_finder(x, y - 1)
  else:
    return 0

#Longest Path DP
def l_path(matrix):
  #Increase memo padding on both sides by 1, not just one side
  memo = [[0 for x in range(len(matrix) + 2)] for y in range(-1, len(matrix) + 2)]
  for i in range(1, len(matrix) + 1):
    for j in range(1, len(matrix) + 1):
      value = matrix[i][j]
      max_val = max(matrix[i+1][j], matrix[i-1][j], matrix[i][j+1], matrix[i][j-1])
      if value - matrix[i+1][j] = 1:
        matrix[i][j] = max_val + 1
      if value - matrix[i-1][j] = 1:
        matrix[i][j] = max_val + 1
      if value - matrix[i][j+1] = 1:
        matrix[i][j] = max_val + 1
      if value - matrix[i][j-1] = 1:
        matrix[i][j] = max_val + 1
      else:
        matrix[i][j] = max_val

  #Memoize, find the max now
  solution = 0
  for i in range(1, len(matrix) + 1):
    for j in range(1, len(matrix) + 1):
      if matrix[i][j] > solution:
        solution = matrix[i][j]
  return solution


#shortest cost recurisve
def min_path(x, y, matrix, cost):
  if x < 0 or y < 0 or x > m - 1 or y > n - 1:
    #this None invalid should kill things - right?
    return
  if (x == m) and (y == n):
    return cost[m][n]
  else:
    #How do the subproblems get eliminated with the mins? How is this not greedy if kill at every step, store in param?
    #This is a really common theme, if you are working with a min subproblem, choosing the next min will always give you the smallest total (no counter example)
    cost = cost[x][y]
    #return min(min_path[x+1][y] + cost, min_path[x][y+1] + cost, min_path[i+1][j+1] + cost) - KEY insight is that THIS is greedy, you choose without context
    #but its okay because we are generating everything and then choosing? If you visit everything it is not even greedy at this point
    #if its [x-1][y] , [x][y-1], is good because given that the past is True, the true min is actually to pick the next min option
    #must go forward to generate
    return min(min_path[x+1][y] + cost, min_path[x][y+1] + cost, min_path[i+1][j+1] + cost)

#Shortest Cost DP
def min_path(matrix, cost):
  memo = [[0 for x in range(len(matrix) + 2)] for y in range(len(matrix[0]) + 2)]
  for i in range(1, len(matrix) + 1):
    for j in range(1, len(matrix) + 1):
      memo[i][j] = min(
        memo[i-1][j],
        memo[i][j-1],
        memo[i-1][j-1]
      )
  return memo[len(matrix)][len(matrix[0])

