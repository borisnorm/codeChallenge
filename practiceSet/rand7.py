#Given only rand5() implement rand7():


#Rejection Sampling
  #just sum does not work
def rand7():
  while True:
    adder = rand5()
    if adder < 3:
      return adder + rand5()

#Geometric Appraoch
def rand7():
  matrix = [ [] [] [] [] [] ]
  return matrix[rand5()][rand5()]

#Average and floor divide
def rand7():
  sum = 0:
  for i in range(0, 5):
    sum += rand5()
  return sum / 7








