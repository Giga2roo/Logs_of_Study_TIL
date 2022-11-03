#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        max_profit = 0
        while right < len(prices):
            currentProfit = prices[right] - prices[left]
            if prices[left] < prices[right]:
                max_profit = max(currentProfit, max_profit)
            else:
                left = right
            right += 1
        return max_profit
        
# @lc code=end


```
input 
- array of `prices` where `prices[i]` is the price of a given stock on the `i`th day.
- maximize profit by choosing a single day to buy one stock and choosing a diffrent day in the future to sell that stock

return
- the maximum profit you can achieve from this transaction

constraints
- 1 <= prices.length <= 10^5
- 0 <= prices[i] <= 10^4
```