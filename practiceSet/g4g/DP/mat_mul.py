#Determine the best sequence to multiply 2 matricies

'''
Given an array p[] which represents the chain of matrices such that the ith matrix Ai is of dimension p[i-1] x p[i].
We need to write a function MatrixChainOrder() that should return the minimum number of multiplications needed to multiply the chain.
 Input: p[] = {40, 20, 30, 10, 30}, a check between the two is a grouping, you can try all grouping, and then do it
  with a list of 3 maritices there is only 1 muiltiplication
'''

#Recursive relationship
def mat_mul(p, i, j):
  if i == j:
    return 0

  min_val = Max_Value
  for k in range(i, j):
    #Divide and split into two groups
    #start to k mid point, and k to end point - where k changes recursively
    #This is how you generate perm groupings
    temp = mat_mul(p, i, k) + mat_mul(p, k + 1, j) + p[i-1]*p[k]*p[j]
    if temp < min_val:
      min_val = count
  return min

#DP solution

def mat_mul(p, i, j):
  memo = [[0 for x in range(len(p))] for y in range(len(p))]

  for i in range(2, len(array)):
    for j in range(1, len(array) - i + 1):
      l = i + len(array) - 1:
      memo[i][j] = MAX_INTEGER
      for k in range(j, l - 1 + 1):
        cost = memo[j][k] + m[k + 1][j] + p[i-1]*p[k]*p[j]
        if cost < m[i][j]
          m[i][j] = cost

  return memo[1][len(array)-1]


