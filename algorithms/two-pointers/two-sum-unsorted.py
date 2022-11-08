from typing import List

nums = [3,2,4]
target = 6
nums2 = [2,7,11,15]
target2 = 9

def two_sum(nums: List[int], target: int):
    nums_map = {}
    for idx, num in enumerate(nums):
        mate = target - num
        if num not in nums_map and mate not in nums_map:
            nums_map[num] = idx
        elif mate in nums_map:
            return [nums_map[mate], idx]

    return []

print(two_sum(nums2, target2))
















