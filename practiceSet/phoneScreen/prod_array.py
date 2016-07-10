#Given an array of n integers where n > 1, nums, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i]. Now do this in linear time without using division.

class Solution:

  def product_array(array):
    culm_prod = reduce(lambda x, y: x * y, array)
    for i in range(len(array)):
      array[i] = culm_prod / array[i]
    return array

  #Without division? Cum, on both sides
  def product_array(array):
    solution = [0 for x in range(len(array)):
    for i in range(len(array)):
      solution[i] = reduce(lambda x, y: x*y, array[:i]) * reduce(lambda x, y: x * y, array[i + 1:])
    return solution

