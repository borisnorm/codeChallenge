#These are the tips here
#list1 = [1, 2, 3]
#str1 = ''.join(str(e) for e in list1), if array items are strings there is no need

def iter_r(string):
  return string[::-1]

def reverse(string):
  array = string.split()
  hi = 0
  low = len(string) - 1
  while hi > low:
    array[hi], array[low] = array[low], array[hi]
  return "".join(str(e) for e in array)

def rec_r(string):
  if len(string) == 1:
    return string
  else:
    return rec_r(string[1:]) + string[0]


print rec_r("iamalion")
print iter_r("iamalion")
print rec_r("iamalion")
