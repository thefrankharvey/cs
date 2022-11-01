let [numbers, target] = [[1,2,3,4,5,11,15], 8]

const twoSum = (numbers, target) => {
    let [left, right] = [0, numbers.length - 1];

    while (left < right) {
        const sum = numbers[left] + numbers[right];

        if (sum === target) return [left + 1, right + 1];
        if (sum < target) left++;
        if (sum > target) right--;
    }

    return [-1, -1];
}

console.log(twoSum(numbers, target))



