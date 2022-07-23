class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buyIdx = 0
        selIdx = 0
        profit = 0
        #profit = prices[selIdx] - prices[0]
        for i in range(len(prices)):
            if prices[buyIdx] > prices[i]:
                buyIdx = i
                selIdx = buyIdx
            elif prices[selIdx] < prices[i]:
                selIdx = i
            profit = max(profit, prices[selIdx]-prices[buyIdx])
        if profit <0:
            return 0
        
        return profit