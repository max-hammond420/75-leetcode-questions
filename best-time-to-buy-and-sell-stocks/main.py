class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        most_profit = 0
        for i in range(len(prices)-1):
            for j in range((i+1), len(prices)):
                profit = prices[j] - prices[i]
                if (profit > most_profit):
                    most_profit = profit

        return most_profit
