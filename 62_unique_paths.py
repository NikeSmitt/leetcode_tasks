class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0] * n for _ in range(m)]
        grid[0][0] = 1
        if n > 1:
            grid[0][1] = 1
        if m > 1:
            grid[1][0] = 1
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    if i > 0:
                        grid[i][j] += grid[i-1][j]
                    if j > 0:
                        grid[i][j] += grid[i][j-1]
        return grid[m-1][n-1]
        


if __name__ == '__main__':
    s = Solution()
    print(s.uniquePaths(1, 1))
