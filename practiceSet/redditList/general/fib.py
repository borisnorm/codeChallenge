#Fibbonacci

def rFib(n):
  if n < 2:
    return 1
  else:
    return rFib(n - 1) + rFib(n - 2)

#Make sure I take care of the n + 1 thing - make sure the indicies are correct
def dpFib(n):
  memo = [0 for x in range(n + 1)]
  memo[0] = 1
  memo[1] = 1
  memo[2] = 2
  #Started this from the wrong index
  for i in range(3, n + 1):
    memo[i] = memo[i - 2] + memo[i - 1]
  #I is correct
  return memo[i]

print rFib(5)
print dpFib(5)










