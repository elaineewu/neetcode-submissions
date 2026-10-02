class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for j in range(m)]for i in range(n)]
        dp[0][0] = 1
        for i in range(n):
            for j in range(m):
                if i==j==0:
                    continue
                dp[i][j] = (dp[i-1][j] if i>=1 else 0)+(dp[i][j-1] if j>=1 else 0)
        return dp[-1][-1]