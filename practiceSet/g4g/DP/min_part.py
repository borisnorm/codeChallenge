#Given a subset, return the subset where the subset - the notsubset is min

#RR- this is amazing, multiple recursive solutions to problems
total = sum(array):

#subsum, starts at 0, total starts at the total
def min_part(array, sub_sum, total):
  if len(array) == 0:
    return abs(total - sub_sum)
  else:
    return min(
      #Add the item to your subset or not
      min_part(array[1:], sub_sum += array[0], total)
      min_part(array[1:], sub_sum, total)
    )

#DP
def min_part(array):
  total = sum(array)
  memo = #array of size n + 1 and size sum + 1, start the index at 1

  #Initalize boolean array
  #First column is true
  #Top row, not 0,0 is False

  for i in range(len(array) + 1):
    for j in range(total + 1): #Did not even think about this SNAP!

      memo[i][j] = memo[i-1][j] #Are we at the target without doing anything

      if (array[i-1] <= j): #If this is false?
        memo[i][j] = memo[i-1][j - array[i-1]] #We could include the value to see

  #From boolean find the array difference
    #Find the largest sum, starting from sum/2 where dp array return true
  diff = Math.MAX_INTEGER
  for j in reversed(range(sum/2)):
    #len of the array means to use all of those values
    if memo[len(array)][j] == True:
        return  sum - 2*j

