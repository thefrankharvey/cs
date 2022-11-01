let palindrome = "race a car"

const isPal = (s) => {
    let cleanStr = s.toLowerCase().replace(/[^a-zA-Z0-9]/g, '')
    for(let i = 0;i<=(cleanStr.length-1)/2; i++)
    if(cleanStr[i] != cleanStr[cleanStr.length-1-i]){
        return false
    }
    return true
    // console.log('===')
    // return (cleanStr[i] != cleanStr[cleanStr.length-1-i] ? false : true)

    // let left =0;
    // let right = cleanStr.length-1
    // for(right;right>=left;right--){
    //     if(cleanStr[right]!=cleanStr[left]){
    //         return false
    //     }
    //     left++
    // }
    // return true
}

console.log(isPal(palindrome))
