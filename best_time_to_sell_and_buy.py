# Say you have an array for which the ith element is the price of a given stock on day i.

# If you were only permitted to complete at most one transaction (i.e., buy one and 
# sell one share of the stock), design an algorithm to find the maximum profit.

# Note that you cannot sell a stock before you buy one.

class Solution(object):
    def maxProfit(self, prices):
        
        if len(prices) == 0:
            return 0
        
        max_price = 0
        min_price = prices[0]
        
        for i in range(len(prices)):
            min_price = min(min_price, prices[i])
            diff = prices[i] - min_price
            max_price = max(max_price, diff)
            
        return max_price
