// https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1627871350324_0Unit
// https://www.youtube.com/watch?v=jM2dhDPYMQM
// Given an array, find the average of all subarrays of ‘K’ contiguous elements in it
// brute force
const input = [2, 3, 4, 1, 5]
const kay=2

function find_sum_of_subarrays(k, arr) {
    let highSum = 0;
    for (let winStart = 0; winStart < arr.length - k + 1; winStart++){
      let winEnd = winStart + k;
      let candidate = 0
      for( let j = winStart; j < winEnd; j++) {
        candidate += arr[j]
      }
      if(candidate > highSum){
        highSum = candidate;
      }
    }
    return highSum;
  }
  
  // const result = find_sum_of_subarrays(kay, input);
  // console.log(`sum of subarrays of size K: ${result}`);


// const input = [2, 3, 4, 1, 5]
// const kay=2
// better
function max_sub_array(k, arr){
  let maxSum = 0,
      winSum = 0,
      winStart = 0;

  for(winEnd = 0; winEnd < arr.length; winEnd++){
      winSum += arr[winEnd];
      if (winEnd >= k -1) {
        maxSum = Math.max(maxSum, winSum);
        winSum -= arr[winStart];
        winStart += 1;
      }
  }
  return maxSum
}

// console.log(max_sub_array(kay, input))

  // To reuse the sum from the previous subarray, we will subtract the element going out of the window and add the element now being included in the sliding window

  function find_averages_of_subarrays2(K, arr) {
    const result = [];
    let windowSum = 0.0,
      windowStart = 0;
    for (let windowEnd = 0; windowEnd < arr.length; windowEnd++) {
      windowSum += arr[windowEnd]; // add the next element
      // slide the window, no need to slide if we've not hit the window size of 'k'
      if (windowEnd >= K - 1) {
        result.push(windowSum / K); // calculate the average
        windowSum -= arr[windowStart]; // subtract the element going out
        windowStart += 1; // slide the window ahead
      }
    }
  
    return result;
  }

  const result2 = find_averages_of_subarrays2(5, [1, 3, 2, 6, -1, 4, 1, 8, 2]);
  console.log(`Averages of subarrays of size K: ${result2}`);