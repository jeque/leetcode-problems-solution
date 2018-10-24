class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if prices != []:
            price_low = prices[0]        
        profit = 0        
        profit_max = 0
        for price in prices:
            if price < price_low:
                price_low = price
            else:
                profit_max = max(profit_max, price - price_low)            
        return profit_max