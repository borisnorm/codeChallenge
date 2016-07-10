#Find the edit distance between two strings

#RR
def edit_distance(stringOne, stringTwo):
  if len(stringOne) == 0:
    return len(stringTwo)
  elif len(stringTwo) == 0:
    return len(stringOne)

  #Wrongly implemented LCS instead of edit distance
  if stringOne[0] == stringTwo[0]:
    return max(edit_distance(stringOne[1:], stringTwo), edit_distance(stringOne, stringTwo[1:]))
  else:
    return max(edit_distance(stringOne[1:], stringTwo) + 1, edit_distance(stringOne, stringTwo[1:]) + 1)

#DP
def edit_distance(stringOne, stringTwo):
  #Padding protection here
  memo = [[0 for i in range(len(stringTwo)) + 1] for j in range(len(stringOne)) + 1]:
  for i in range(len(1, stringOne)):
    for j in range(len(1, stringTwo)):
      if stringOne[i] == stringTwo[j]:
        memo[i][j] = min(
          memo[i-1][j],
          memo[i][j-1]
        )
      else:
        memo[i][j] = (
          memo[i-1][j] + 1,
          memo[i][j-1] + 1
        )
  return memo[i][j]

