var threeSum = function(nums) {  
    const results = [];
    const target = 0;
    nums.sort((a,b) => a - b);
  
    for(let i=0; i<nums.length-2; i++){
      if(i > 0 && nums[i] === nums[i-1]) continue;
      let left = i+1;
      let right = nums.length-1;
  
      while(left<right){
        let sum = nums[i]+nums[left]+nums[right];
        
        if(sum > target){ 
          right--;
        }
        else if(sum < target){ 
          left++;
        }
        else{ 
          results.push([nums[i],nums[left],nums[right]])
          while(nums[left] === nums[left+1]) left++;
          while(nums[right] === nums[right-1]) right--;
          left++
          right--
        }
      }
  
    }
    return results;
  };