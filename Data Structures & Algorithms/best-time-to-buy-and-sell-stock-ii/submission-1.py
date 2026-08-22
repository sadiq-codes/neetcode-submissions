class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        for i in range(1, len(prices)):
            sell = prices[i]
            buy = prices [i - 1]
            if buy < sell:
                profit = sell - buy
                maxP += profit
            else:
                continue
        return maxP
