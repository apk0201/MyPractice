class Solution:
    def solve(self, a, b):
        a = int(a)
        b = int(b)
        c = a+b
        d = a*b
        return str(c), str(d)


a = input("Enter an integer: ")
b = input("Enter another integer: ")

str_add = Solution()
print(str_add.solve(a,b))
