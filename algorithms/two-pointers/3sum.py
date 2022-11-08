from typing import List
# Given an integer array nums
# return all the triplets [nums[i], nums[j], nums[k]] 
# such that i != j, i != k, and j != k
# and nums[i] + nums[j] + nums[k] == 0

# must NOT contain duplicate triplets.
nums = [-1,0,1,2,-1,-4]
#                   h 
#      [-4, -1, -1, 0, 1, 2]  
#            i  l   
target = 0
# Output: [[-1,-1,2],[-1,0,1]]

def threeSum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    result = []
    for i, num in enumerate(nums):
        if nums[i] > 0:
            break
        if nums[i-1] != nums[i]:
            lo = i+1
            high = len(nums)-1
            while lo < high:
                sum = nums[i] + nums[lo] + nums[high]
                if sum > target:
                    high -=1
                elif sum < target:
                    lo+=1
                else:
                    result.append([nums[i], nums[lo], nums[high]])
                    while nums[lo] == nums[lo+1]: lo+=1
                    while nums[high] == nums[high-1]: high-=1
                    lo+=1
                    high-=1

    return result


print(threeSum(nums))