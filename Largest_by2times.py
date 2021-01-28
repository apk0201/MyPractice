import math


class Solution:
    def solve(self, nums):
        a = int(max(nums))
        nums.sort()
        b = nums[-2]
        if a > 2*b:
            return True
        else:
            return False


nums = [2,3,9]
large = Solution()
print(large.solve(nums))