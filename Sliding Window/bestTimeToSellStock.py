class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit,minTillNow = -sys.maxsize - 1,sys.maxsize
        for price in prices:
            minTillNow = min(minTillNow,price)
            profit = max(profit, price-minTillNow)
        return profit