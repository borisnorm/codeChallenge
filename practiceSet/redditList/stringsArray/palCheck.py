def palCheck(string):
  low = 0
  hi = len(string) - 1
  while hi > low:
    if string[hi] != string[low]:
      return False
    #dont for get to change the counter
    hi -= 1
    low += 1
  return True

print palCheck("tacocat")
print palCheck("ryanhang")

