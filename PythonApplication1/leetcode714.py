#714. 买卖股票的最佳时机含手续费
#动态规划
class Solution:
    def maxProfit(self, prices, fee):
        n = len(prices)
        #初始化，不买0元，买了就是-prices[0]元
        dp = [[0, -prices[0]]] + [[0, 0] for _ in range(n - 1)]
        for i in range(1, n):
            #第i天手里没有股票，说明前一天也没有，或者今天卖掉
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i] - fee)
            #第i天手里有股票，说明前一天有股票，或者今天买入
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])
        #最后一天卖出
        return dp[n - 1][0]