#Key Insight is y = x ^ 1/2, y^2 = x
#Runtime complexity for this problem too

def square_root(number):
  solution = 1
  while !(solution * solution + 1 <= number <= solution * solution - 1):
    if (number > solution * solution + 1):
      solution = solution + .1
    if (numner < solution * solution - 1):
      solution = solution - .1
  return solution
#Convergence rate within the bound, hard complexity













