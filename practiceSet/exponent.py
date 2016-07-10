#Think of the edge cases you might need to test
def expo_easy(number, pow):
  counter = pow
  solution = number
  if (pow == 0):
    return 1
  while (counter > 0):
    solution = solution * solution
    counter -= 1
  if (pow > 0):
    return solution
  if (pow < 0):
    return 1 / solution

 #Expo hard bit shifting solution










