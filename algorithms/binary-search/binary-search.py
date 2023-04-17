# https://algo.monster/problems/binary_search_intro
# https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1628743417172_1Unit
# https://www.tryexponent.com/courses/software-engineering/data-structures/binary-search
# https://www.techinterviewhandbook.org/algorithms/sorting-searching/
# vanilla binary search
from typing import List
from numpy import sort
import math

input = [1, 2, 3, 4, 6, 9, 11, 14, 29, 35]
target=11


def binary_search(arr: List[int], target: int) -> int:
    arr.sort()
    print(arr)
    low = 0
    high = len(arr)-1

    while low <= high:
        mid = math.floor((low + high) / 2)
        print('MID: ', mid)
        guess = arr[mid]
        print('GUESS: ', guess)
        if guess == target:
            print(guess, ' <<<< its the guess')
            return mid
        if guess > target:
            high = mid - 1
            print('HIGH: ', high)
        if guess < target:
            low = mid + 1
            print('LOW: ', low)
    return None

# binary_search(input, target)

# find the boundary
# https://algo.monster/problems/binary_search_boundary

# if the element is false, we discard everything to the left and the current element itself.
# if the element is 'true', the current element could be the first true although there may be other true to the left. We discard everything to the right but what about the current element
# record current element in the range then discard it

#  keep a variable boundary_index that represents the leftmost true's index currently recorded 
# If the current element is true - update boundary_index with its index and discard everything to the right including the current element itself since its index has been recorded by the variable.

input = [False, False, False, False, False, True, True]
def find_boundary(arr: List[bool]) -> int:
    left, right = 0, len(arr)-1
    boundary_index = -1

    while left <= right:
        mid = math.floor((left + right) / 2)
        if arr[mid]:
            boundary_index = mid
            right = mid - 1
        else:
            left = mid + 1
    print(boundary_index)
    return boundary_index

# find_boundary(input)

def search(nums: List[int], target: int) -> int:
    left, right = 0, len(nums)-1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] > target:
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            return mid
    return -1

nums = [-1,0,3,5,9,12]
target = 9
# print(search(nums, target))
# // leetcode Runtime: 266 ms, faster than 84.24% of Python3 online submissions for Binary Search.
# // Memory Usage: 15.4 MB, less than 72.77% of Python3 online submissions for Binary Search.

# First Element Not Smaller Than Target
# Given an array of integers sorted in increasing order and a target, find the index of the first element in the array that is larger than or equal to the target. Assume that it is guaranteed to find a satisfying number.
def first_not_smaller(arr: List[int], target: int) -> int:
    left, right = 0, len(arr)-1
    boundary_index = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            boundary_index = mid
            right = mid - 1
        else:
            left = mid + 1
    return boundary_index

nums = [1, 3, 3, 5, 8, 8, 10]
target = 1

# print(first_not_smaller(nums, target))

# Given a sorted array of integers and a target integer, find the first occurrence of the target and return its index. Return -1 if the target is not in the array.


# Input:
# arr = [1, 3, 3, 3, 3, 6, 10, 10, 10, 100]
# target = 3
# Output: 1

def find_first_occurrence(arr: List[int], target: int) -> int:
    left, right = 0, len(arr)-1
    candidate = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            candidate = mid
            right = mid - 1
        else:
            left = mid + 1
    return candidate

arr = [1, 3, 3, 3, 3, 6, 10, 10, 10, 100]
target = 10
# print(find_first_occurrence(arr, target))

# first try
# def square_root(n: int) -> int:
#     spread_n = list(range(n))
#     print(spread_n)
#     left, right = 0, math.ceil(n / 2)
#     print(left, ' ', right)
#     candidate = -1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] * arr[mid] > n:
#             right = mid - 1
#             print('right: ', right, '\n')
#         else:
#             left = mid + 1
#     return right

def square_root(n: int) -> int:
    if n == 0 or n == 1:
        return n
    left, right = 1, n
    candidate = -1
    while left <= right:
        mid = (left + right) // 2
        if mid * mid <= n:
            candidate = mid
            left = mid + 1
        else:
            right = mid - 1
    return candidate

target = 13

# print(square_root(target))

arr = [3,9,8,6,4]
def peak_of_mountain_array(arr: List[int]) -> int:
    if len(arr) < 3:
        return 0
    candidate = -1
    left, right = 0, len(arr)-1

    while left < right:
        mid = (left+right) // 2
        if arr[mid] < arr[mid+1]:
            left = mid + 1
        else:
            candidate = mid
            right = mid
    return candidate

print(peak_of_mountain_array(arr))



def find_min_rotated(arr: List[int]) -> int:
    # WRITE YOUR BRILLIANT CODE HERE
    return 0