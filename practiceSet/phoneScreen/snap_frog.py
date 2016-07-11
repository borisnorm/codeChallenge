#Given array, frog crossing a river,
#it can jum same as prev, one more, one less, can the frog make it

class Solution:

    #target should be initialized as len(array) - 1
    #current index is 0, prev jump is 0

    #Recursive solution
    def jump_path(array, curr_index, prev_jump, target):
        if curr_index = target:
            return True
        if index < 0:
            return False
        if index >= len(array):
            return False
        else:
            return jump_path(array, curr_index + prev_jump, prev_jump, target)
                or jump_path(array, curr_index + prev_jump - 1, prev_jump - 1, target)
                or jump_path(array, curr_index + prev_jump + 1, prev_jump + 1, target)

    #Dp no idea

