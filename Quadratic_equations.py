# given a list of integers nums sorted in ascending order, and integers a, b, and c.
# Apply the following function for each number x in nums: ax^2 + bx + cax 2 +bx+c
# and return the resulting list in ascending order.


class Solution:
    def solve(self, nums, a, b, c):
        n = len(nums)
        lst = []
        for i in range(n):
            y = a * (nums[i] ** 2) + b * nums[i] + c
            lst.append(y)
            y == 0
        lst.sort()
        return lst


nums = [-2, 3]
a, b, c = 1, -3, 2
s = Solution()
print(s.solve(nums, a, b, c))
