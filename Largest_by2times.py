# Given a list of integers nums,
# return whether the largest number is bigger than the second-largest number by more than two times.


import math


class Solution:
    def solve(self, nums):
        a = int(max(nums))
        nums.sort()
        b = nums[-2]
        if a > 2 * b:
            return True
        else:
            return False


nums = [2, 3, 9]
large = Solution()
print(large.solve(nums))
