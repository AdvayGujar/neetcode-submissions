class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyPointer = 0
        sellPointer = 0
        profit = 0
        isRunning = True

        for sellPointer in range(len(prices)):
            tempProfit = prices[sellPointer] - prices[buyPointer]
            if tempProfit > profit:
                profit = tempProfit
            
            if prices[sellPointer] < prices[buyPointer]:
                buyPointer = sellPointer

        return profit