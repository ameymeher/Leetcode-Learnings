# Leetcode-Learnings
Essential learning from Leetcode problems

| # | Summary | Comments | References |
|---|---------|----------|------------|
| 1 | Efficient operations based on if input from a stream or a list | - Better to do sort on the complete list <br> - If possible do bucket sort for input from a stream <br> - Basically, see how you can optimize for these two scenarios | [Minimum Time Difference - Bucket Sort](Algorithms/Minimum%20Time%20Difference%20-%20Bucket%20Sort.py) |
| 2 | If the size of a data structure is fixed, consider array too instead of using a general data structure | - Had to implement a Deque with fixed size <br> I choose the data structure as a double ended linked list <br> - It was correct, but since the size is fixed, can also use an array <br> - Keep an eye out for a simple solution rather than a general one | [Circular Deque](./Data%20Structures/Circular%20Deque.py) | 
| 3 | Rain water problems mostly can be solved with Two pointers | - I solved it using monotonic stack, which was also good <br> - There was a two pointer solution which was more amazing<br> - Column wise adding the water and row wise adding the water | 1. [Trapping Rain Water](./Two%20Pointers/Trapping%20Rain%20Water.py) <br>2. [Trapping Rain Water - Monotonic Stack](./Monotonic%20Stack/Trapping%20Rain%20Water.py) |
| 4 | Palindrome questions, Inwards from the end or Outwards from the center | - I struggled with the expanding from the center for this question, but coming inwards from the ends was way too easy. | [Valid Palindrome II](./Palindrome/Valid%20Palindrome%20II.py) 
| 5 | Equation logic of two-sum, i+j=target <br> i = target - j <br> Find if there was such i <br> | - Can be used in general problems involving two iterations and getting a fixed value, usually going O(N^2) because of two loops <br>- By checking if the previous was there or not in a hashmap helps <br>- In this problem, was used with a prefix sum, a crazy problem | [Make Sum divisible by p](./Prefix%20Sum/Make%20Sum%20divisible%20by%20p.py) 
| 6 | Think about prefix and suffixes in sentences too | - Idiotically tried a hashset solution here <br> - Prefix Suffix logic was so clean <br> - Need to actively think about these | [Sentence Similarity III](./String%20Manipulations/Sentence%20Similarity%20III.py)