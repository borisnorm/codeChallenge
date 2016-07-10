#Find the longest increase subsequence in an array

#Recursive solution, generate all sub sequences to see if they are increasing
#Generate all sub sequences, one could start at each unique point in time
#Generate a subsequence at a starting index, or string

#Recursive relation
#initalize sub_sequence as an empty array, Initalize at every index in the array? Some optimizations, cut length
def lis(array, sub_sequence):
  if len(array) == 0:
    return len(sub_sequence)
  #if the thing you need to add to the array > then the item to be added
  if array[0] <= sub_sequence[len(sub_sequence) - 1]:
    return
  #Add or do not add the sequence, everything is valid up to this point
  return max(
    lis(array[1:], sub_sequence += array[0]),
    lis(array[1:], sub_sequence)

#DP soltuion, is the compelxity the same?
def lis(array):
  #memo = [[0 for i in range(len(array) + 1)] for j in range(len(array)) + 1]
  #MEMO is 1d, whyyy

  #Watch out for this string indexing, substring might start here
  for i in range(len(array)):
    for j in range(0, i):

      #if
      #pointer 1 is larger than pointer 2
      #length of i's run is not that large? Dont know the second one1
      if array[i] > array[j] and memo[i] < memo[j] + 1:
        memo[i] = memo[j] + 1
  return max(memo)






      #The comparisons will always be one directional
      if array[j] > array[i]:
        memo[i][j] += 1
      else:
      #we need to involve the strings in some way
        memo[i][j] = max(
          memo[i-1][j-1]
          memo[i-1][j]
          memo[i][j-1]
        )
  #Return the max of the end columns?
  return memo[i][j]

