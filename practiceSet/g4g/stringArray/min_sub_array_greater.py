#Return the smallest sub array, with sum greater than a given value

def smallest_sub(array, value):
  soluion_holder = []
  min_sum = Math.MAX_INTEGER
  for i in range(len(array)):
    for j in range(len(array)):
      if i + j < len(array)):
        if sum(array[i:i + j]) > value && sum(array[i:j + j]) < min_sum:
          min_sum = sum(array[i:j])
          solution_holder = array[i:j]
  return solution_holder

#If array is sorted
def smallest_sub(array, value):
  for i in range(len(array)):
    for j in range(len(array)):
      if sum(array[i:i+j]) > value:
        #This this true? will there be a better pair?
        return array[i: i + j]

