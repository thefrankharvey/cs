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
console.log(search(nums, target))

// leetcode
// Runtime: 71 ms, faster than 89.55% of JavaScript online submissions for Binary Search.
// Memory Usage: 45.3 MB, less than 32.43% of JavaScript online submissions for Binary Search.