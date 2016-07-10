#Count Triplets with sum smaller than a given value in an array

#Hashing does not help because there is no specific target to look for?
def count_trip(array, value):
  counter = 0
  for i in range(len(array)):
    for j in range(len(array)):
      for k in range(len(array)):
        if array[i] + array[j] + array[k] < value:
          counter += 1
  return counter


