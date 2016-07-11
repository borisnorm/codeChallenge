#Find first non duplicate item in a string in linear time

from collection import defaultdict

class Solution:

    def non_duplicate(string):
        frequency = defaultdict(int)
        for i in string:
            frequency[i] += 1

        for i in string:
            if frequency[i] == 1:
                return i
        return -1

