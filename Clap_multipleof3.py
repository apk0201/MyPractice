class Solution:
    def solve(self, n):
        s = "clap"
        l = ['3','6','9']
        list1 = list(range(1, n+1))
        for i in range(len(list1)):
            if list1[i] % 3 == 0:
                list1[i] = s
            for j in range(len(l)):
                if str(list1[i]).__contains__(l[j]):
                    list1[i] = s
            list1[i] = str(list1[i])
        return list1


n = int(input("enter number:"))
clap = Solution()
print(clap.solve(n))
