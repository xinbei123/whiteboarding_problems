# Given a 2d grid map of '1's (land) and '0's (water), count the number of islands.
#  An island is surrounded by water and is formed by connecting adjacent lands horizontally 
#  or vertically. You may assume all four edges of the grid are all surrounded by water.

class Solution(object):
    def numIslands(self, grid):

        counter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    self.helper(grid, i, j)
                    counter += 1
        return counter
                    
    def helper(self,grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] == '0':
            return
            
        grid[i][j] = '0'
        self.helper(grid, i-1, j)
        self.helper(grid, i, j+1)
        self.helper(grid, i+1, j)
        self.helper(grid, i, j-1)
