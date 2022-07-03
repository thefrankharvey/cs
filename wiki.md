# CS | Algorithms and Datastructures | Practice problems
*compiled from algomonster, techinterviewhandbook (free), udemy, designgurus, multiple books* 

## Highest ROI Concepts (algomonster)
- [AlgoMonster](https://algo.monster/problems/stats)
1. 2 pointers
2. BFS
3. DFS
4. Binary Search
5. Priority Queue

## Basic Maths Cheatsheet
- [AlgoMonster](https://algo.monster/problems/math-basics)
1. Logarithms
    - log(8) = 3
    - divide 8 by 2 three times to get to 1
2. Permutations and Factorial
    - n * (n-1) * (n-2)... 1
    - 5! = 5 * 4 * 3 * 2 * 1 = 120
3. Subsets
    - num of options * num of options (n times)
    - if 1 switch has 2 states on/off
        - then 2 ^ 1 = 2
    - if 2 switches have 2 states
        - then 2 ^ 2 = 4
    - if 4 switches have 3 states
        - then 3 states ^ 4 switches
        - 3 (states) * 3 (states) * 3 (states) * 3(states) =  81 (total states / options)
4. Arithmetic sequence (diff between each element is same)
    - [1,3,5,7,9,11,13]
    - sum of an arithmetic sequence is (first_element + last_element) * number_of_element / 2
    - (1 + 13) * 7 / 2
        - (14) * 7 / 2
            - 98 / 2
                - 49
    - `n = 10`
    `for (i = 0; i < 10; i++) {`
        `for (j = 0; j <= i; j++) {`
            `doSomething();`
        `}`
    `}`
    - This is an arithmetic sequence and the total run time is O(n^2)
    - the sum can be expressed as (2 * first_element + difference * (number_of_elements - 1)) * number_of_element)
    - In big O complexity analysis, we drop the constant terms (first_element and diffence, so this really becomes O(n^2)
    - :( Major WTF
5. Mod
    - **if x < y, return x**
    - else subtract y from x until x < y
    - `function mod(x, y) {`
        `while (x >= y) {`
            `x -= y`
        `}`
     `return x`
    `}`
    - MOD property often used in interview questions for *distributivity*:
    - E.g. [30, 20, 150, 110, 200]
    - find the two integers whose sum is divisible by 60
    - (a + b) MOD c = ((a MOD c) + (b MOD c)) MOD c
        - so (a + b) % 60 == 0 is equivalent to (a % 60 + b % 60) % 60 == 0
        - %60 on each number in the array gets [30, 20, 30, 50, 20] and 30 + 30 = 60
    - :\ Kinda WTF

## Runtime Cheatsheet - God help me
- [AlgoMonster](https://algo.monster/problems/runtime_summary)
- Nope

## Data Structures
1. Stacks
    - [AlgoMonster](https://algo.monster/problems/stack_intro)
    - [Udemy](https://www.udemy.com/course/master-the-coding-interview-data-structures-algorithms/learn/lecture/12332948#overview)
    - [TechInterviewHandbook](https://www.techinterviewhandbook.org/algorithms/stack/)
    <br />
    - LIFO - 'last in first out'
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
    - Corner cases
        1. Empty stack. Popping from an empty stack
        2. Stack with one item
        3. Stack with two items

    - ### Practice
        Basic
        1. [valid parens](https://leetcode.com/problems/valid-parentheses/)
        2. [queue using stacks](https://leetcode.com/problems/implement-queue-using-stacks/)

        Pro
        [advanced problems](https://www.techinterviewhandbook.org/algorithms/stack/#recommended-practice-questions)

