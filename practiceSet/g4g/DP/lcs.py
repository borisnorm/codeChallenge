#Find the longest common subseqence between two strings

#Recurisve Relation
def lcs(stringOne, stringTwo):
  if len(strinOne) == 0 or len(stringTwo) == 0:
    return 0
  if stringOne[0] == stringTwo[0]:
    return lcs(stringOne[1:], stringTwo[1:]) + 1
  else:
    return max(
      lcs(stringOne[1:], stringTwo),
      lcs(stringOne, stringTwo[1:]
    )

#DP Solution
def lcs(stringOne, StringTwo):
  memo = [[0 for x in range(len(stringOne) + 1)] for y in range(len(stringTwo) + 1)]
  #protect the overflow?
  for i in range(1, len(stringOne)):
    for j in range(1, len(stringTwo)):
      else if stringOne[i] == stringTwo[j]:
        memo[i][j] += 1
      else:
        memo[i][j] = max(
          memo[i-1][j-1],
          memo[i-1][j],
          memo[i][j-1]
        )
  return memo[i][j]

