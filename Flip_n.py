class Solution:
    def solve(self, n):
        s1 = str(n)
        l1 = []
        s2 = ""
        l2 = []
        for i in range(len(s1)):
            l1.append(s1[i])
        set1 = set(l1)
        if n > 0:
            for i in range(len(l1)):
                if int(l1[i]) < 3:
                    l1[i] = '3'
                    s2 = s2.join(l1)
                    break
        if set1 == {'3'}:
            s2 = s2.join(l1)
        if n < 0:
            for i in range(1, len(l1)):
                if int(l1[i]) > 3:
                    l1[i] = '3'
                    break
            s2 = s2.join(l1)
        return int(s2)


n = int(input("enter number to flip: "))
flip = Solution()
print(flip.solve(n))


