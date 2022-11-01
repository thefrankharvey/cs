






let arr = [0,0,1,1,1,1,2,2,3,3,4,5]



function removeDuplicates(arr) {
    slow = 0
    for(let fast = 1; fast < arr.length; fast++){
        if(arr[fast] != arr[slow]){
            slow++
            arr[slow] = arr[fast]
        }
    }
    return arr
}

console.log(removeDuplicates(arr))