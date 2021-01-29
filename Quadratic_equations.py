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


nums = [-2,3]
a, b, c = 1, -3, 2
s = Solution()
print(s.solve(nums, a, b, c))
