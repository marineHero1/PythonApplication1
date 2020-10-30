#463. 岛屿的周长

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rows=len(grid)
        cols=len(grid[0])
        sum1=0
        for i in range(rows):
            for j in range(cols):
                if(grid[i][j]==0):
                    continue
                up=1 if i==0 else (1 if grid[i-1][j]==0 else 0)
                down=1 if i==rows-1 else (1 if grid[i+1][j]==0 else 0)
                left=1 if j==0 else (1 if grid[i][j-1]==0 else 0)
                right=1 if j==cols-1 else (1 if grid[i][j+1]==0 else 0)
                sum1=sum1+up+down+left+right
        return sum1

#test=Solution()
#res=test.islandPerimeter([[0,1,0,0], [1,1,1,0], [0,1,0,0], [1,1,0,0]])
#print(res)