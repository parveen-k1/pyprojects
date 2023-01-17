from typing import List
class FloodFill:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        Row = len(image)
        Col = len(image[0])
        fill_color = image[sr][sc]
        if fill_color == color:
            return image
        def dfs(row, col):
            if image[row][col] == fill_color:
                image[row][col] = color
                if row >= 1:
                    dfs(row - 1, col)
                if row + 1 < Row:
                    dfs(row + 1, col)
                if col >= 1:
                    dfs(row, col - 1)
                if col + 1 < Col:
                    dfs(row, col + 1)
        
        dfs(sr, sc)
        return image


a = FloodFill()
b = a.floodFill(image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2)
print(b)