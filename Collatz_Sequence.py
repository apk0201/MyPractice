class Solution:
    def solve(self, n):
        list1 = [n]

        while n != 1:
            if n % 2 == 0:
                n = n / 2
                list1.append(n)
            else:
                n = 3 * n + 1
                list1.append(n)
        return len(list1)


n = int(input("Enter number: "))
a = Solution()
print(a.solve(n))
