class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        buyPrice = prices[0]

        for i in range(len(prices)):
            if prices[i] < buyPrice:
                buyPrice = prices[i]

            sell = prices[i]
            profit = sell - buyPrice
            maxProfit = max(profit, maxProfit)

        return maxProfit

                

            
