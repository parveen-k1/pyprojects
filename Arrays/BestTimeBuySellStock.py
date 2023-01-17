from typing import List
import sys
class BestTimeBuySellStock:
    def maxProfit(self, prices: List[int]) -> int:
        smallest = sys.maxsize
        difference = 0
        for i in range(len(prices)):
            if prices[i] < smallest:
                smallest = prices[i]
            difference = max(difference, prices[i] - smallest)
        return difference

a = BestTimeBuySellStock()
b = a.maxProfit(prices = [7,1,5,3,6,4])
print(b)