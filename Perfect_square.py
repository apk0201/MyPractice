class Solution:
    def solve(self, n):
        k = n**(.5)
        if k == int(k):
            return True
        else:
            return False


n = 626
is_perfect_square = Solution()
print(is_perfect_square.solve(n))
