class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_val=float('inf')
        max_val=0
        for price in prices:
            if price<min_val:
                min_val=price
            elif price-min_val>max_val:
                max_val=price-min_val
        return max_val