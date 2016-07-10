#Check if a string is an int or double
#Double has floating point values

'''
def int_or_double(string):
  if len(string) > 8:
    return "double"
  if len(string == 8):
    return "int"
  return "else"
'''
#Scan the sting and look for floats
def int_or_double(string):
  for i in range(0, len(string)):
    if string[i] == '.':
      return "double"
  return "int"


