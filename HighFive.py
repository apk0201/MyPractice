# Given an integer n,
# return the maximum number you can make by inserting 5 anywhere in the number.


class Solution:
    def solve(self, n):
        s1 = str(n)
        s2 = ""
        list1 = []
        for i in range(len(s1)):
            list1.append(s1[i])
        if n >= 0:
            for i in range(len(list1)):
                if int(list1[i]) < 5:
                    list1.insert(i, '5')
                    break
            n = int(s2.join(list1))
        else:
            b = False
            for i in range(1, len(list1)):
                if int(list1[i]) > 5:
                    list1.insert(i, '5')
                    b = True
                    break
            if not b:
                list1.append('5')
            n = int(s2.join(list1))
        return n


n = int(input("Enter number: "))
hf = Solution()
print(hf.solve(n))

