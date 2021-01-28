class Solution:
    def solve(self, s):
        if s == s[::-1]:
            return True
        return False


s = input("enter word to check is it palindrome or not: ")
is_palindrome = Solution()
if is_palindrome.solve(s):
    print("Yes")
else:
    print("No")
