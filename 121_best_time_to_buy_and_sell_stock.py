# You are given an array prices where prices[i] is the price of a given stock on the ith day.
#
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the
# future to sell that stock.
#
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        lowest_price = float('inf')
        profit = 0
        
        for i in range(len(prices)):
            if prices[i] < lowest_price:
                lowest_price = prices[i]
                
            profit = max(profit, prices[i] - lowest_price)
        
        return profit

if __name__ == '__main__':
    s = Solution()
    assert 5 == s.maxProfit([7, 1, 5, 3, 6, 4])
    assert 0 == s.maxProfit([7, 6, 4, 3, 1])
    assert 3 == s.maxProfit([2, 1, 4])
    
    print('All Tested!!!!')
