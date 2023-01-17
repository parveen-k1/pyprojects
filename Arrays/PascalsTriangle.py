from typing import List
class PascalsTriangle:
    def generate(self, numRows: int) -> List[List[int]]:
        ans = [[1]]
        for i in range(1, numRows):
            tri = [1]
            for j in range(1, i):
                tri.append(ans[i-1][j] + ans[i-1][j-1])
            tri.append(1)
            ans.append(tri)
        return ans


a = PascalsTriangle()
b = a.generate(5)
print(b)