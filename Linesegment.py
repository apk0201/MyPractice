class Solution:
    def solve(self, coordinates):
        n = len(coordinates)
        l1 = []
        try:
            for i in range(n):
                if i != n - 1:
                    x1 = coordinates[i][0]
                    y1 = coordinates[i][1]
                    x2 = coordinates[i + 1][0]
                    y2 = coordinates[i + 1][1]
                else:
                    x1 = coordinates[i][0]
                    y1 = coordinates[i][1]
                    x2 = coordinates[0][0]
                    y2 = coordinates[0][1]
                m = (y2 - y1) / (x2 - x1)
                l1.append(m)
            set1 = set(l1)
            if len(set1) == 1:
                return True
            else:
                return False
        except ZeroDivisionError:
            return False


coord = [[1, 7], [3, 7], [7, 7]]
line = Solution()
print(line.solve(coord))
