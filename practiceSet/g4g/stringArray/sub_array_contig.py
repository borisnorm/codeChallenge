#length of largest sub array with contiguous elements
#Given an array of distinct integers, find length of the longest subarray which contains numbers that can be arranged in a continuous sequence.

#Non duplicate
def cont_check(array):
  sorted_array = sorted(array)
  for i in range(1, len(sorted_array)):
    if sorted_array[i] - sorted_array[i - 1] != 1
      return False
  return True

def sub_array(array):
  max_len = 1
  for i in range(len(array)):
    for j in range(len(array)):
      #remember i + j for the substrings! EEEEK!
      if cont_check(array[i:i + j]) && len(array[i:i + j]) > max_len:
        max_len = len(array[i: i+j])
  return max_len

#I dont think that you can sort (1, 100, 200, 2, 300, 400, 5, 600, 700)
#How do we check for duplicates?




