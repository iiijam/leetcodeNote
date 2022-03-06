'''
给定一个数组 prices ，其中 prices[i] 表示股票第 i 天的价格。

在每一天，你可能会决定购买和/或出售股票。你在任何时候 最多 只能持有 一股 股票。你也可以购买它，然后在 同一天 出售。
返回 你能获得的 最大 利润 。

输入: prices = [7,1,5,3,6,4]
输出: 7
解释: 在第 2 天（股票价格 = 1）的时候买入，在第 3 天（股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。
     随后，在第 4 天（股票价格 = 3）的时候买入，在第 5 天（股票价格 = 6）的时候卖出, 这笔交易所能获得利润 = 6-3 = 3 。

输入: prices = [7,6,4,3,1]
输出: 0
解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
'''

class Solution:
    def maxProfit(self, prices: list[int]) -> int:
#if len prices == 0 or 1, profit = 0
        if len(prices) <= 1:
            profit = 0
        else:
#if prices[i] > prices[i-1], profit = prices[i] - prices[i-1]
            profit = 0
            for i in range(1, len(prices)):
                if prices[i] > prices[i-1]:
                    tempProfit = prices[i] - prices[i-1]
                    profit += tempProfit
        return profit

print(Solution().maxProfit([7,1,5,3,6,4]))