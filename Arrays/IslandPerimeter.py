from typing import List
class IslandPerimeter:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        result = 0
        for r in range(0, rows):
            for c in range(0, cols):
                if grid[r][c] == 1:
                    result += 4
                    if r > 0 and grid[r - 1][c] == 1:
                        result -= 2
                    if c > 0 and grid[r][c - 1] == 1:
                        result -= 2
        return result

a = IslandPerimeter()
b = a.islandPerimeter(grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]])
print(b)