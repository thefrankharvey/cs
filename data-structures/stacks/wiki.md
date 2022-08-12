## Stacks
- [AlgoMonster](https://algo.monster/problems/stack_intro)
- [Udemy](https://www.udemy.com/course/master-the-coding-interview-data-structures-algorithms/learn/lecture/12332948#overview)
- [TechInterviewHandbook](https://www.techinterviewhandbook.org/algorithms/stack/)
- LIFO - 'last in first out'
- can only add and remove elements to them from one side
- use arrays or singly linked lists
- 3 operations
    - **Push** = into the stack
    - **Peek** = look at top item (last inserted item)
    - **Pop** = remove top item
    - **isEmpty** = check if empty
    - **Size** = returns num of elements
- *Recursion* and *DFS* use stack
- Overflow (inserting when stack is full) and underflow errors (inserting on empty stack = check if stack is empty first)
- Insertion and deletion from the list have a time complexity of O(1) (on average)
- Search is O(n) = has to search each of the n elements
- ### Corner cases
    1. Empty stack. Popping from an empty stack
    2. Stack with one item
    3. Stack with two items