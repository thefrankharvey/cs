var isValid = function(s) {
    stack = []
    openers = ['[', '{', '(']
    for (const char of s) {
        if (openers.includes(char)) {
            stack.push(char)
            }
        else {
            if (stack.length === 0) {
                return false
            }
            top = stack.pop()
            if (
                (top === '{' && char != '}') || 
                (top === '[' && char != ']') || 
                (top === '(' && char != ')')
            ) {
                return false
        }
    }
}
    return (stack.length === 0) ? true :false
};

console.log(isValid('()[]'))
// LeetCode: 07/02/2022 20:29 Accepted 58 ms, faster than 97.81% of JavaScript online submissions for Valid Parentheses