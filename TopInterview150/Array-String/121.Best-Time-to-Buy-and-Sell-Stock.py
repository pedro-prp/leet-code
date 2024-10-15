class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell, profit = 0, 1, 0

        while sell < len(prices):
            if prices[buy] < prices[sell]:
                local_profit = prices[sell] - prices[buy]
                profit = max(profit, local_profit)
            else:
                buy = sell
            sell += 1

        return profit
