#qSort to handle 3 pointers

#Handle repeated cases?

def partition(array, i, j):
  if len(array) == 1:
    return
  hi = j #why the -1?
  lo = i + 1
  pivot = array[i]

  while True:
    #I NEED to center things around the pivot, seek thingsS
    #WHILE CONDITIONS WERE FLIPPED
    while (array[lo] < pivot):
      lo += 1
    while (array[hi] > pivot):
      hi -= 1
    #swap the pivot with hi and continue
    #pivot must be returned
    if lo > hi:
      array[i], array[hi] = array[hi], array[i]
      print array
      return hi
    array[lo], array[hi] = array[hi], array[lo]
    hi -= 1
    lo += 1

#qSort
def qSort(array, lo, hi):
  if abs(lo - hi) <= 1:
    return array
  else:
    index = partition(array, lo, hi)
    #is this +1 and -1 a good idea? Does this work?
    qSort(array, lo, index - 1)
    qSort(array, index + 1, hi)

test = [22, 333, 0, -22, 1000]
#parition seems to be correct for sure
#print partition(test, 0, len(test) - 1)
print qSort(test, 0, len(test) - 1)
