class Solution:
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = [[False] * cols for _ in range(rows)]

        def dfs(r, c):
            # Check bounds and if the cell is water or already visited
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 'W' or visited[r][c]:
                return
            
            # Mark the current cell as visited
            visited[r][c] = True
            
            # Explore all four possible directions
            dfs(r + 1, c)  # down
            dfs(r - 1, c)  # up
            dfs(r, c + 1)  # right
            dfs(r, c - 1)  # left

        island_count = 0
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 'L' and not visited[i][j]:
                    # Found an unvisited landmass, which means a new island
                    dfs(i, j)
                    island_count += 1
        
        return island_count

# Testing the Solution class
if _name_ == "_main_":
    solution = Solution()
    
    # Test case 1
    result1 = solution.getTotalIsles([
        ["L", "L", "L", "L", "W"],
        ["L", "L", "W", "L", "W"],
        ["L", "L", "W", "W", "W"],
        ["W", "W", "W", "W", "W"]
    ])
    print(result1)  # Output: 1

    # Test case 2
    result2 = solution.getTotalIsles([
        ["L", "L", "W", "W", "W"],
        ["L", "L", "W", "W", "W"],
        ["W", "W", "L", "W", "W"],
        ["W", "W", "W", "L", "L"]
    ])
    print(result2)  # Output: 3
