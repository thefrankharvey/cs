from typing import List
arr= [1, 2, 3, 4, 5, 7, 8, 11, 18]
target = 12     
# Output: 1 3

# sorted arrr ints
# target
# 2 numbs add to target
# return indices
# 0n

#  **list comp to eliminate right side where > target

def twoSum(nums: List[int], target) -> List[int]:
    left, right = 0, len(nums)-1
    while right > left:
        two_sum = nums[left] + nums[right]
        if two_sum == target:
            return [left, right]
        if nums[right] > target or two_sum > target:
            right-=1
        else:
            left+=1

print(twoSum(arr, target))
