from turtle import end_fill
from typing import List

    # find lowest price
    # find the highest price after lowest
    # find the max diff
        # buy price - sell price

# Return the maximum profit you can achieve from this transaction
# If you cannot achieve any profit, return 0.


prices = [7,3,1,5,3,6,4]
# Output: 5
# 5
# what defines max profit
# begins with the LOWEST buy number - i
# if its the lowest keep track as min so far
# if it is NOT the lowest get the difference
# ask what is the lowest/best buy day
#  the keep track of LARGEST difference
# keep track of lowest num
def maxProfit(prices: List[int]) -> int:
    max_profit = 0
    min_so_far = 100000
    for price in prices:
        if price < min_so_far:
            min_so_far = price
        else:
            candidate = price - min_so_far
            max_profit = max(max_profit, candidate)
    
    return max_profit

# brute force
# def maxProfit(prices: List[int]) -> int:
#     output = 0
#     left = 0
#     while left < len(prices):
#         right=left+1
#         while right < len(prices): 
#             profit = prices[right]-prices[left]
#             if profit > output:
#                 output = profit
#             right+=1
#         left+=1
    
#     return output

print(maxProfit(prices))