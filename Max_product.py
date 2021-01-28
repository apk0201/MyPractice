class Solution:
    def solve(self, nums):
        list1 = []
        for i in nums:
            for j in range(0, len(nums)):
                if nums.index(i) != j:
                    n1 = i * nums[j]
                    list1.append(str(n1))
        for i in range(len(list1)):
            list1[i] = int(list1[i])
        list1.sort()
        max = list1[-1]
        if max != 0:
            return max
        else:
            return "product is zero"


nums_string = input("enter a list element seperated by space:")
nums = nums_string.split()
for i in range(len(nums)):
    nums[i] = int(nums[i])
max_prod = Solution()
print(max_prod.solve(nums))