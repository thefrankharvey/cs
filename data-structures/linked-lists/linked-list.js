class Node {
    constructor(val, next = null) {
        this.val = val;
        this.next = next;
    }
}

class LinkedList {
    constructor() {
      this.head = null;
      this.tail = null;
      this.length = 0;
    }

    insert(value) {
        this.length++;
        let newNode = new Node(value);
      
        if (this.tail) {
          this.tail.next = newNode;
          this.tail = newNode;
          return newNode;
        }
      
        this.head = this.tail = newNode;
        return newNode;
      }
    
    remove() {
    if (this.tail) {
        this.length--;
    
        const tailNode = this.tail;
    
        // search for the node before tail
        let currentNode = this.head;
    
        // The while loop stops when the node next to tail node is found
        while (currentNode.next != tailNode) {
        currentNode = currentNode.next;
        }
    
    
        const beforeTail = currentNode;
        this.tail = beforeTail;
        this.tail.next = null;
    
        return tailNode;
    }
    return undefined;
    }

    print() {
    let current = this.head;
    while (current) {
        console.log(current.value);
        current = current.next;
    }
      }
  }

const linkedList = new LinkedList();
linkedList.insert(7);
linkedList.insert(20);
linkedList.insert(42);
linkedList.insert(7116);
linkedList.insert(2001);
console.log(linkedList)