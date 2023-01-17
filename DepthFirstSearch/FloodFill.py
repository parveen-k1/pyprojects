from typing import List
class FloodFill:
    def dfs(self, image, r, c, col, color):
        if r >= 0 and c >= 0 and r < len(image) and c < len(image[0]) and image[r][c] == col and image[r][c] != color:
                image[r][c] = color
                self.dfs(image, r - 1, c, col, color )
                self.dfs(image, r + 1, c, col, color)
                self.dfs(image, r, c - 1, col, color)
                self.dfs(image, r, c + 1, col, color)

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        fill_color = image[sr][sc]
        if fill_color == color:
            return image
        self.dfs(image, sr, sc, fill_color, color)
        return image


a = FloodFill()
b = a.floodFill(image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2)
print(b)