class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profits=[]
        minimum=0
        maximum=1
        if len(prices)==1:
            return 0
        while maximum<len(prices):
            profits.append(prices[maximum]-prices[minimum])
            if prices[maximum]<prices[minimum]:
                minimum=maximum
            maximum+=1
        profit=max(profits)
        if profit<=0:
            return 0
        else:
            return profit