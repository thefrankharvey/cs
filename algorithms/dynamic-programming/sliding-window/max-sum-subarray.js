// https://designgurus.org/path-player?courseid=grokking-the-coding-interview&unit=grokking-the-coding-interview_1627871350324_0Unit
// https://www.youtube.com/watch?v=jM2dhDPYMQM
// Given an array, find the average of all subarrays of ‘K’ contiguous elements in it
// brute force
// const input = [1, 3, 2, 6, -1, 4, 1, 8, 2]
// const kay=5

function find_averages_of_subarrays(K, arr) {
    const result = [];
    for (let i = 0; i < arr.length - K + 1; i++) {
      // find sum of next 'K' elements
      let sum = 0.0;
      for (let j = i; j < i + K; j++) {
        sum += arr[j];
      }
      result.push(sum / K); // calculate average
    }
  
    return result;
  }
  
  const result = find_averages_of_subarrays(5, [1, 3, 2, 6, -1, 4, 1, 8, 2]);
  console.log(`Averages of subarrays of size K: ${result}`);

  // To reuse the sum from the previous subarray, we will subtract the element going out of the window and add the element now being included in the sliding window

  function find_averages_of_subarrays2(K, arr) {
    const result = [];
    let windowSum = 0.0,
      windowStart = 0;
    for (let windowEnd = 0; windowEnd < arr.length; windowEnd++) {
      windowSum += arr[windowEnd]; // add the next element
      // slide the window, no need to slide if we've not hit the window size of 'k'
      if (windowEnd >= K - 1) {
        console.log('start', windowStart)
        console.log('element', arr[windowStart])
        console.log('end', windowEnd)
        console.log('element', arr[windowEnd])
        result.push(windowSum / K); // calculate the average
        console.log('1window sum', windowSum)
        windowSum -= arr[windowStart]; // subtract the element going out
        console.log('2window sum', windowSum)
        windowStart += 1; // slide the window ahead
      }
    }
  
    return result;
  }

  const result2 = find_averages_of_subarrays2(5, [1, 3, 2, 6, -1, 4, 1, 8, 2]);
  console.log(`Averages of subarrays of size K: ${result2}`);
  10