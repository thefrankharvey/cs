
from typing import List


arr2 = [0, 0, 0, 2, 7, 0, 0, 9, 0, 0]
arr = [0, 1]

def move_zeroes(nums: List[int]) -> None:
    slow,fast = 0,1
    while(fast <= len(nums)-1):
        if(nums[fast] > 0 and nums[slow] == 0):
            nums[fast], nums[slow] = nums[slow], nums[fast]
            slow+=1

        fast+=1

def move_zeroes2(nums: List[int]) -> None:
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]
            slow += 1

print(arr2)
move_zeroes2(arr2)
print(arr2)