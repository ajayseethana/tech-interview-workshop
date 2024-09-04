# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):

        low = 1
        high = n

        while low <= high:
            middle = int((low + high) / 2)
            result = guess(middle)

            if result == -1:
                high = middle - 1

            elif result == 1:
                low = middle + 1
        
            else:
                return middle
