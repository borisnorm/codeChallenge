#Find alll pythag triplets in an array

def py_trip(array):
  solution = []
  sorted_array = sorted(array)
  hypot = defaultdict(int)
  for i in sorted_array:
    hypot[i ** 2] = i

  for j in array:
    for k in array:
      if hypot[( j ** 2 + k ** 2 )] > 0:
        solution.append(j, k, hypot[j ** 2 + k ** 2])

  return solution













