## Arrays
- [AlgoMonster](https://algo.monster/problems/binary_search_first_element_not_smaller_than_target)
- [Udemy](https://www.udemy.com/course/master-the-coding-interview-data-structures-algorithms/learn/lecture/12300322#overview)
- [TechInterviewHandbook](https://www.techinterviewhandbook.org/algorithms/array/)
- [Exponent](https://www.tryexponent.com/courses/software-engineering/data-structures/arrays)

Basic
- removing, inserting, or finding arbitrary values in an array can be a linear-time operation
- to find subarrays use sliding window
- sliding window is a subset of dynamic programming

Pros
- fast lookups
- fast push pop
- ordered-elements close in memory

Cons
- slow inserts
- slow deletes
- fixed size if static array

Tips
- Don’t use an array if you need to search for unsorted items efficiently or insert and remove items frequently
- If you're asked to operate on a sorted array, you may want to consider using the 2 pointer technique
    - one pointer as a fast-runner and the other as a slow-runner
    - or you may place one pointer at the beginning and the other at the end