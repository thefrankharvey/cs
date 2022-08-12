class Node {
    constructor(value){
        this.value = value;
        this.next = null
    }
}

class Queue {
    constructor(){
        this.first = null;
        this.last = null;
        this.length= 0;
    }
    peek() {
        console.log('peeking', this.first)
        return this.first
    }
    enqueue(value) {
        console.log('enqueue ', value)
        const newNode = new Node(value)
        console.log('new node made ', newNode)
        if (this.length === 0) {
            this.first = newNode
            this.last = newNode
        } else {
            const prevLast = this.last
            console.log('prevLast', prevLast)
            prevLast.next = newNode
            console.log('prevLast.next', prevLast.next)
            this.last = newNode
            console.log('this.last - new last', this.last)
        }
        this.length++
        console.log('linked list queue: ', this)
        return this
    }
    dequeue(){
        if (this.first) {
            this.first = this.first.next
            this.length--;
            return this
        }
        return null;
    }
    isEmpty(){
        console.log(this.first == null)
        return this.first == null
    }
}

const myQueue = new Queue();
myQueue.enqueue('google')
myQueue.enqueue('udemy')
myQueue.enqueue('discord')
myQueue.enqueue('netflix')
myQueue.peek()
myQueue.dequeue()
myQueue.peek()
myQueue.dequeue()
myQueue.peek()
myQueue.isEmpty()
myQueue.dequeue()
myQueue.peek()
myQueue.dequeue()
myQueue.peek()
myQueue.isEmpty()