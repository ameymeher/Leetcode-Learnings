# Leetcode-Learnings

## My mistakes and learnings

| # | Summary | Comments | References |
|---|---------|----------|------------|
| 1 | Efficient operations based on if input from a stream or a list | - Better to do sort on the complete list <br> - If possible do bucket sort for input from a stream <br> - Basically, see how you can optimize for these two scenarios | [Minimum Time Difference - Bucket Sort](Algorithms/Minimum%20Time%20Difference%20-%20Bucket%20Sort.py) |
| 2 | If the size of a data structure is fixed, consider array too instead of using a general data structure | - Had to implement a Deque with fixed size <br> I choose the data structure as a double ended linked list <br> - It was correct, but since the size is fixed, can also use an array <br> - Keep an eye out for a simple solution rather than a general one | [Circular Deque](./Data%20Structures/Circular%20Deque.py) | 
| 3 | Rain water problems mostly can be solved with Two pointers | - I solved it using monotonic stack, which was also good <br> - There was a two pointer solution which was more amazing<br> - Column wise adding the water and row wise adding the water | 1. [Trapping Rain Water](./Two%20Pointers/Trapping%20Rain%20Water.py) <br>2. [Trapping Rain Water - Monotonic Stack](./Monotonic%20Stack/Trapping%20Rain%20Water.py) |
| 4 | Palindrome questions, Inwards from the end or Outwards from the center | - I struggled with the expanding from the center for this question, but coming inwards from the ends was way too easy. | [Valid Palindrome II](./Palindrome/Valid%20Palindrome%20II.py) 
| 5 | Equation logic of two-sum, i+j=target <br> i = target - j <br> Find if there was such i <br> | - Can be used in general problems involving two iterations and getting a fixed value, usually going O(N^2) because of two loops <br>- By checking if the previous was there or not in a hashmap helps <br>- In this problem, was used with a prefix sum, a crazy problem | [Make Sum divisible by p](./Prefix%20Sum/Make%20Sum%20divisible%20by%20p.py) 
| 6 | Think about prefix and suffixes in sentences too | - Idiotically tried a hashset solution here <br> - Prefix Suffix logic was so clean <br> - Need to actively think about these | [Sentence Similarity III](./String%20Manipulations/Sentence%20Similarity%20III.py)
| 7 | Using Generators in Python | - Crazy good if you want to keep the state of the function and also return something out of it <br> - Makes the code more manageable and clean <br> - Useful to create an iterator object | 1. [Nested List Weight Sum](./Generators/Nested%20List%20Weight%20Sum.py) <br> 2. [Flatten Nested List Iterator](./Stack%20/Flatten%20Nested%20List%20Iterator.py)
| 8 | Utilizing constriants to use Greedy approach <br> Reduced complexity from O(N^2) to O(N) | - I implemented this problem using O(N^2) loops, meanwhile a crazy greedy approach existed <br> - It utilized the constraint that we wanted the rightmost larger number, and the leftmost smaller one <br> - In one iteration, we can figure this out | [Maximum Swap](./String%20Manipulations/Maximum%20Swap.py) 
| 9 | Truncate division towards zero <br> use int(a/b) <br> // and math.floor truncates towards - infinity | - I used math.floor here, but -1.5 truncates to -2. I wanted -1. <br> - For this, use int(a/b) or math.trunc(a/b) | [Basic Calculator II](./String%20Manipulations/Basic%20Calculator%20II.py)
| 10 | While dealing with reverse expressions, remember to reverse the numbers that are formed <br> Take comprehensive test cases, forgot to take 2 digit numbers | - For this problem, I reversed the expression <br> - After forming the numbers, I was directly appeding it, forgot to reverse the number formed <br> - Always take good test cases, forgot to consider two digit numbers | [Basic Calculator](./String%20Manipulations/Basic%20Calculator.py)
| 11 | Recursive solution is top down, iterative solution is bottom up, atleast in this case | - I solved it using a recursive approach <br> - The iterative approach is also so simple using a stack and starting from the bottom up | [Evaluate Reverse Polish Notation](./String%20Manipulations/Evaluate%20Reverse%20Polish%20Notation.py)


## Patterns in problems you just need to know

| # | Summary | Comments | References |
|---|---------|----------|------------|
| 1 | Getting the next permutation of a string | - Start from the back of the string to get the char which is not in increasing order <br> - Find the character to the right of it which is just greater than that character <br> - Swap these two <br> - Reverse all the characters after the char we just found not in increasing order to start from the start | [Next Permutation](./String%20Manipulations/Next%20Permutation.py)