class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profit = 0
        for i in range(len(prices)):
            if i == 0:
                buy = prices[i]
            elif prices[i] < buy:
                buy = prices[i]
            else:
                 if profit < prices[i] - buy:
                    profit = prices[i] - buy
        
        return profit