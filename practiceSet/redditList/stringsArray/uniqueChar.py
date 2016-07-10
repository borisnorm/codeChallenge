#Find if string has all unique char
#in place, is n squared, linear time with linear memory is also a way

def allUnique(string):
  lookup = set()
  for i in range(len(string)):
    if string[i] in lookup:
      return False
    lookup.add(string[i])
  return True

print allUnique("abcedrfgh")
print allUnique("asdfbkeiga")










