const get_each_fib = (n) => {
    let fib_list = []
    const range = [...Array(n).keys()]
    const fib = n => n<2 ? n : fib(n-2) + fib(n-1)
    for (num in range) fib_list.push(fib(parseInt(num)))

    return fib_list
}

const nums = [1,2,3,4,5,6,7,8,9,10,12,19,21,39,43,44,46,79,80,81]

const get_odds = nums => {
    const result = []
    const isOdd = n => (n % 2) === 0 ? true : result.push(n)
    const rec = nums => {
        if(nums.length > 0){
            isOdd(nums.shift())
            rec(nums)
        }
        return true
    }
    rec(nums)
    return result
}

console.log(get_odds(nums))