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

// LeetCode: 07/02/2022 20:29 Accepted 58 ms, faster than 97.81% of JavaScript online submissions for Valid Parentheses

// Object oriented stack implementation

// Linked list node
class Node {
    constructor(value){
        this.value = value;
        this.next = null
    }
}

class Stack {
    constructor(){
        this.top = null;
        this.bottom = null;
        this.length= 0;
    }
    peek() {
        console.log('peeking', this.top)
        return this.top
    }
    push(value) {
        console.log('pushing ', value)
        const newNode = new Node(value)
        console.log('new node made ', newNode)
        if (this.length === 0) {
            this.top = newNode
            this.bottom = newNode
        } else {
            const oldTop = this.top
            this.top = newNode
            this.top.next = oldTop
        }
        this.length++
        console.log('linked list stack: ', this)
        return this
    }
    pop(){
        if (!this.top) {
            return null
        }
        this.top = this.top.next
        this.length--;
        return this;
    }
    isEmpty(){
        return this.top == null
    }
}

const myStack = new Stack();
myStack.push('google')
myStack.push('udemy')
myStack.push('discord')
myStack.push('netflix')
myStack.peek()
myStack.pop()
myStack.pop()
myStack.pop()
myStack.peek()
myStack.pop()
myStack.peek()
myStack.isEmpty()