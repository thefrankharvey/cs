var search = function(nums, target) {
    let left= 0;
    let right= nums.length-1;
    
    while(left <= right) {
        let mid= Math.ceil( (left + right) / 2)

        if(nums[mid] < target){
            left= mid + 1;
        } else if(nums[mid] > target) {
            right= mid - 1;
        } else {
            return mid
        }
    }
    return -1;
};

nums= [-1,0,3,5,9,12]
target= 13
// console.log(search(nums, target))

// leetcode
// Runtime: 71 ms, faster than 89.55% of JavaScript online submissions for Binary Search.
// Memory Usage: 45.3 MB, less than 32.43% of JavaScript online submissions for Binary Search.

// peak mountain
var peakIndexInMountainArray = function(arr) {
    let candidate = -1;
    let left = 0;
    let right = arr.length - 1;

    if(arr.length < 3) {
        return candidate
    }

    while(left <= right){
        mid = Math.floor((left + right) / 2)
        if(arr[mid] < arr[mid-1]){
            right = mid-1
        }
        else{
            candidate = mid
            left = mid + 1
        }
        return right
    }
};

const arr = [0,1,2,9,7,5,2,1,0]
console.log(peakIndexInMountainArray(arr))