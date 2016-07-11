#Move all zeros to the right of array, in place
i need a pointer at the end, and i will scan the array
from opposite ends, and then swap and increment, if they are same then return the array
i

def (nums):

left = 0
right = len(nums) - 1

while True:
    while num[i] != 0:
    	left += 1

    nums[left], nums[right] = nums[left], nums[right]
    right -= 1
    if left > right:
	return nums



