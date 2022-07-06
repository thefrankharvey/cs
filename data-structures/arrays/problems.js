// more problems
// https://www.udemy.com/course/master-the-coding-interview-data-structures-algorithms/learn/lecture/12310382#overview

// reverse a string

function reverseString(str) {
    let reversed = ''
    // check input
    if (!str || str.length < 2 || typeof str !== 'string') {
        return 'pass a string with multiple letters'
    }
    for (i = str.length-1; i >= 0; i--) {
        reversed += str[i];
    }
    console.log(reversed)
    return reversed;
}


reverseString('hello')

function reverse2(str) {
    return str.split('').reverse().join('')
}

const reverse3 = str => [...str].reverse.join('')

// merge sorted arrays

array1 = [0,1,3,7,28]
array2 = [2,5,9,30]

function mergeArrays(arr1, arr2) {
    // check input
    // is array? is 2 params? 1 or both arrays empty?
    let merged = [...arr1, ...arr2];
    let sorted = merged.sort((a, b) => a - b)
    return sorted
}

// mergeArrays(array1, array2)

// diff arrays
// https://www.tryexponent.com/courses/software-engineering/swe-practice/difference-of-arrays

// define the problem - search problem

a = [1, 2, 3]
b = [2, 4, 6]

function diff(nums1,nums2){
    const start = performance.now()
    // check input
    if (!Array.isArray(nums1) || !Array.isArray(nums2) || nums1.length == 0 || nums2.length == 0) {
        console.log('pass two valid nonempty arrays')
        return 'pass two valid nonempty arrays'
    }

    // solve purely using sets - hideous but faster by than array solve by 50% - perf 0.02 ms
    const setA = new Set(nums1)
    const setB = new Set(nums2)
    let diffs = []
    let result = []

    for (const val of setA) {
        if (!setB.has(val)) {
            result.push(val)
        }
    }
    diffs.push(result)
    result = []

    for (const val of setB) {
        if (!setA.has(val)) {
            result.push(val)
        }
    }
    diffs.push(result)
    result = []

    const duration = performance.now() - start
    console.log(duration)
    console.log(diffs)
    return diffs
}

// Runtime: 164 ms, faster than 65.79% of JavaScript online submissions
// Memory Usage: 49 MB, less than 35.53% of JavaScript online submissions

// solve 2 - combo of array filter and sets
var findDifference = function(nums1, nums2) {
    if (!Array.isArray(nums1) || !Array.isArray(nums2) || nums1.length == 0 || nums2.length == 0) {
        return 'pass two valid nonempty arrays'
    }
    result = []

        let difference = nums1
                 .filter(x => !nums2.includes(x))
        result.push(Array.from(new Set(difference)))
                    
        difference = nums2
             .filter(x => !nums1.includes(x))
        result.push(Array.from(new Set(difference)))

    return result
};

findDifference(a,b)

// Runtime: 172 ms, faster than 61.05% of JavaScript online submissions
// Memory Usage: 48.6 MB, less than 52.89% of JavaScript online submissions