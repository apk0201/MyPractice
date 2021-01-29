# Given a list of integers nums and an integer k,
# return the maximum possible i where nums[0] + nums[1] + ...  + nums[i] ≤ k.
# Return -1 if no valid i exists.


class Solution:
    def solve(self, nums, k):
        a = 0
        index = 0
        n = len(nums)
        if n != 0:
            for i in range(n):
                if a <= k:
                    a = a + nums[i]
                    index = i
                if a > k:
                    return i - 1
                    break
            return index
        else:
            return -1


nums = []
k = 0
k_prefix = Solution()
print(k_prefix.solve(nums,k))