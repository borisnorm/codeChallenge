#Given a sorted array and a number x, find the pair in array whose sum is closest to x

def close_pair(array, target):
  min_distance = 10000
  best_pair = None
  sorted_array = sorted(array)
  for i in sorted_array:
    for j in sorted_array:
      #Optional optimization - There should always be an improvement if sorted?
      #Why is the complexity cut down when sorted? from n2 to n3
      if abs(target - ( i + j ) ) > min_distance:
        return best_pair

      if abs(target - (i + j)) < min_distance:
        min_distance = abs(target - (i + j))
        best_pair = (i, j)
  return best_pair







