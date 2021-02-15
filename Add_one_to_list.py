# given a list of integers nums, representing a decimal number and nums[i] is between [0, 9].
# For example, [1, 3, 9] represents the number 139.
# Return the same list in the same representation except modified so that 1 is added to the number.

class Solution:
    def solve(self, nums):
        nums_str = ""
        for i in range(len(nums)):
            nums[i] = str(nums[i])
        if nums:
            nums_str = nums_str.join(nums)
            str_number = int(nums_str)
            add_one_num = str_number + 1
            nums = list(str(add_one_num))
            for i in range(len(nums)):
                nums[i] = int(nums[i])
            return nums
        else:
            return [1]


nums = [9]
after_adding_one = Solution()
print(after_adding_one.solve(nums))
