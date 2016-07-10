#Given a distance ‘dist, count total number of ways to cover the distance with 1, 2 and 3 steps.

#distance, and array of steps in the step count
  #1, 2, 3 is specific - general case is harder because of hard coding

#RR solution
def cover(distance):
  if distance < 0:
    return 0
  if distance = 0:
    return 1
  else:
    return cover(distance - 1) + cover(distance - 2) + cover(distance - 3)

#DP solution
def cover(distance):
  memo = [0 for x in range(distance) + 1]
  memo[1] = 1
  memo[2] = 2
  memo[3] = 3
  for i in range(4, len(distance)):
    #I am not sure if i need to add anything onto this or not, no add because its the same number of ways - we are not counting total number of step
    #we can do that too
    memo[i] = memo[i-1] + memo[i -2] + memo[i-3]
  return memo[distance]

