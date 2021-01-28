import math


class Solution:
    def solve(self, words, letters):
        l1 = []
        l2 = []
        for i in words:
            fail = False
            for j in i:
                lhs = count_char(j, i)
                rhs = count_char(j, letters)
                if lhs > rhs:
                    fail = True
                    break
            if not fail:
                l1.append(i)
        if len(l1) !=0:
            for i in l1:
                len1 = len(i)
                l2.append(str(len1))
            for i in range(len(l2)):
                l2[i] = int(l2[i])
            length = max(l2)
            return int(length)
        else:
            return 0


def count_char(ch, word):
    count = 0
    for i in word:
        if i == ch:
            count += 1
    return count


words_string = input("enter a list element seperated by space:")
words = words_string.split()
letters = input("enter letters string: ")
form = Solution()
print(form.solve(words, letters))
