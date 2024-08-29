class Solution:
    def countSubIslands(self, grid1, grid2):
        def dfs(i, j):
            if i < 0 or i >= len(grid2) or j < 0 or j >= len(grid2[0]) or grid2[i][j] == 0:
                return True

            # If the current cell in grid1 is water while grid2 is land, it can't be a sub-island
            if grid1[i][j] == 0:
                return False

            # Mark the cell as visited in grid2
            grid2[i][j] = 0

            # Continue DFS in 4 directions and check if all parts of the island are valid
            up = dfs(i - 1, j)
            down = dfs(i + 1, j)
            left = dfs(i, j - 1)
            right = dfs(i, j + 1)

            # An island in grid2 is a sub-island only if all of its parts are valid
            return up and down and left and right

        m, n = len(grid2), len(grid2[0])
        count = 0

        # Iterate through grid2
        for i in range(m):
            for j in range(n):
                # When a land cell is found in grid2, we start DFS
                if grid2[i][j] == 1:
                    if dfs(i, j):
                        count += 1

        return count
