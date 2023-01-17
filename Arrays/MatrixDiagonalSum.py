from typing import List
class MatrixDiagonalSum:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum = 0
        n = len(mat)
        for i in range(n):
            sum += mat[i][i] + mat[n - 1 - i][i]
        if n % 2 == 1:
            sum -= mat[n//2][n//2]
        return sum


a = MatrixDiagonalSum()
b = a.diagonalSum(mat = [[1,2,3],[4,5,6],[7,8,9]])
print(b)