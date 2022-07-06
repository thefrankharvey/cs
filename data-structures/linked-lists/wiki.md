## Linked Lists
- [Visualgo](https://visualgo.net/en/list)
- [Udemy](https://www.udemy.com/course/master-the-coding-interview-data-structures-algorithms/learn/lecture/12320368#overview)
- [TechInterviewHandbook](https://www.techinterviewhandbook.org/algorithms/linked-list/)

Basics
- Linear data structure
- Scattered/Dynamic memory allocation vs arrays (contiguous static block of memory)
- More info
    - [basecs](https://medium.com/basecs/whats-a-linked-list-anyway-part-1-d8b7e6508b9d)
- Pros
    - **Insertion/Deletion** = O(1) - no indexing / shifting of elements
    - **Dynamic** - can grow or shrink as needed w/out given size of memory allocated
- Cons
    - **Traversal** = O(n) - access/search - cannot access by index


- ### Common Routines
    1. Counting the number of nodes in the linked list
    2. Reversing a linked list in-place
    3. Finding the middle node of the linked list using two pointers (fast/slow)
    4. Merging two linked lists together
- ### Corner cases
    1. Empty linked list (head is null)
    2. Single node
    3. Two nodes
    4. Linked list has cycles. Tip: Clarify beforehand with the interviewer whether there can be a cycle in the list. Usually the answer is no and you don't have to handle it in the code
- ### Techniques
    1. **Sentinel/dummy nodes**
        - Adding a sentinel/dummy node at the head and/or tail might help to handle many edge cases where operations have to be performed at the head or the tail. The presence of dummy nodes essentially ensures that operations will never have be done on the head or the tail, thereby removing a lot of headache in writing conditional checks to dealing with null pointers. Be sure to remember to remove them at the end of the operation.
    2. **Two pointers**
        - Getting the kth from last node - Have two pointers, where one is k nodes ahead of the other. When the node ahead reaches the end, the other node is k nodes behind
        - Detecting cycles - Have two pointers, where one pointer increments twice as much as the other, if the two pointers meet, means that there is a cycle
        - Getting the middle node - Have two pointers, where one pointer increments twice as much as the other. When the faster node reaches the end of the list, the slower node will be at the middle
    3. **Using space**
        - Many linked list problems can be easily solved by creating a new linked list and adding nodes to the new linked list with the final result. However, this takes up extra space and makes the question much less challenging. The interviewer will usually request that you modify the linked list in-place and the solve the problem without additional storage
        - [LeetCodeReverseLinkedList](https://leetcode.com/problems/reverse-linked-list/)

- ### Practice Questions
    - Essential [TechInterViewHandbook](https://www.techinterviewhandbook.org/algorithms/linked-list/#essential-questions)
    - Advanced [TechInterViewHandbook](https://www.techinterviewhandbook.org/algorithms/linked-list/#recommended-practice-questions)