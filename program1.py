class Solution:
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        # Edge case: If the grid is empty, return 0
        if not grid or not grid[0]:
            return 0
        
        # Get the dimensions of the grid
        rows, cols = len(grid), len(grid[0])
        
        # Function to perform DFS to mark the entire island as visited
        def dfs(r, c):
            # If we are out of bounds or at water, stop recursion
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == 'W':
                return
            # Mark the land as visited (change 'L' to 'W')
            grid[r][c] = 'W'
            # Explore all 4 possible directions (up, down, left, right)
            dfs(r - 1, c)  # up
            dfs(r + 1, c)  # down
            dfs(r, c - 1)  # left
            dfs(r, c + 1)  # right

        # Initialize island count
        island_count = 0
        
        # Traverse through each cell in the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 'L':  # Found an unvisited land
                    island_count += 1   # It's a new island
                    dfs(r, c)           # Perform DFS to mark the whole island
        
        return island_count

# Test case 1
grid1 = [
    ["L","L","L","L","W"],
    ["L","L","W","L","W"],
    ["L","L","W","W","W"],
    ["W","W","W","W","W"]
]
# There is a single large connected landmass, so the output should be 1.
print(Solution().getTotalIsles(Solution, grid1))  # Output: 1  

# Test case 2
grid2 = [
    ["L","L","W","W","W"],
    ["L","L","W","W","W"],
    ["W","W","L","W","W"],
    ["W","W","W","L","L"]
]
# There are three separate islands: one large island at the top left, one in the middle, and one at the bottom right.
print(Solution().getTotalIsles(Solution, grid2))  # Output: 3  
