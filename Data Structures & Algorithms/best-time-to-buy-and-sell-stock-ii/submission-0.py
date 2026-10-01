class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #dp[i][j] means profit up till day i if I am holding j {0,1}
        #dp[0][0] = 0 
        #dp[0][1] = -prices[i]
        #reccurence means that 
        n = len(prices)
        dp = [[0]*2 for _ in range(len(prices))]
        dp[0][0] = 0 
        dp[0][1] = -prices[0]

        for i in range(1,len(prices)):
            dp[i][0] = max(dp[i-1][0],dp[i-1][1]+prices[i]) 
            dp[i][1] = max(dp[i-1][1],dp[i-1][0]-prices[i])
        return max(dp[n-1][0],dp[n-1][1])
        