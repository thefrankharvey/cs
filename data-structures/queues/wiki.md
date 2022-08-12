## Stacks
- [TechInterviewHandbook](https://www.techinterviewhandbook.org/algorithms/queue/)
- [AlgoMonster](https://algo.monster/problems/queue_intro)
- [Udemy](https://www.udemy.com/course/master-the-coding-interview-data-structures-algorithms/learn/lecture/12334448#overview)
- FIFO - First In First Out
- enqueue - 'add element to one end'
- dequeue - 'remove element to one end'
- can be implemented as arrays or singly linked lists
- most languages don't have queues - use arrays or lists
- say that you assume that there's a queue data structure to use which has an efficient enqueue operation
- They often use a dynamic array as its underlying data structure (although they can also use a double-linked list, like Python's deque class
- time complexity
    - **Enqueue/Offer** = O(1)
    - **Dequeue/Poll** = O(1)
    - **Front** = O(1)
    - **Back** = O(1)
    - **isEmpty** = O(1)
    - **lookup** = O(n)
- ### Corner cases
    1. Empty queue
    2. Queue with one item
    3. Queue with two items
- Consider using a queue whenever you need to process items in the order you receive them, or use a stack for the reverse order. Common real-world applications include graph search algorithms, web crawlers, and storing application history (“undo/redo”)
- typically arrays are used to build fixed-size stacks and queues, whereas linked lists are used to build variable-sized stacks and queues