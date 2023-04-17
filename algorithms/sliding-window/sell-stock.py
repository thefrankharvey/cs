from typing import List

prices = [7,3,1,5,3,6,4]
# notice peaks and valleys - imagine a graph/chart
# break down to binary decision
# what do we need to know - what is lowest and what is hightest diff
# is this minimum?
# if so add to min tracker - if lowest record it
# if not - operate - subtract min from this num - record as largest diff
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

print(maxProfit(prices))



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