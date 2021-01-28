class Solution:
    def solve(self, nums, a, b, c):
        n = len(nums)
        lst = []
        for i in range(n):
            y = a * (nums[i] ** 2) + b * nums[i] + c
            lst.append(str(y))
            y == 0
        for i in range(len(lst)):
            lst[i] = int(lst[i])
        lst.sort()
        return lst


nums = [-2,3]
a, b, c = 1, -3, 2
s = Solution()
print(s.solve(nums, a, b, c))
