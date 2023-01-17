from typing import List
from collections import deque
class FloodFill:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
        shift = [0, 1, 0, -1, 0]
        oldColor = image[sr][sc]
        image[sr][sc] = color
        queue = deque([(sr, sc)])
        while queue:
            (r, c) = queue.popleft()
            for k in range(0, 4):
                x = r + shift[k]
                y = c + shift[k + 1]
                if x < 0 or y < 0 or x > len(image)-1 or y > len(image[0])-1 or image[x][y] == color or image[x][y] != oldColor:
                    continue
                image[x][y] = color
                queue.append((x, y))
        return image

a = FloodFill()
b = a.floodFill(image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2)
print(b)