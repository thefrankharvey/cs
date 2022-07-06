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

mergeArrays(array1, array2)