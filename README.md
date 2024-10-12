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
| 12 | Finding if two intervals intersect | - end1 >= start2 <br> - end2 >= start1 | [Interval List Intersections](./Interval%20problems/Interval%20List%20Intersections.py)
| 13 | Modulus behavior of python <br> a%b has the same sign as b | - a%b gives the result with the same sign as b <br> - If b is negative, then the result will be negative <br> If b is positive, then the result will be positive <br> - -1%26 = 25 | [Group Shifted Strings](./Maths/Group%20Shifted%20Strings.py) <br> [Rotary Clock](./Assessment%20questions/Meta/Level%201/Rotary%20Clock.py)
| 14 | Good practice for division operation | - Trick was to consider only k+1 block <br> - Also to find the number of spaces remaining <br> - (a-b) gives the number of spaces with one of a and b included <br> - (a-b-1) gives the number of spaces between these two numbers <br> - (a-b+1) gives the number of spaces including these two numbers | [Cafeteria](./Assessment%20questions/Meta/Level%201/Cafeteria.py)
| 15 | Read the question and test on sample input first <br> Used a HashMap earlier, but had to use a Set | - Here, had to keep a track of the last k dishes eaten, not the last k dishes <br> - Used a HashMap to maintain the counts, but instead had to just maintain the type of dishes eaten, by a HashSet | [Kaitenzushi](./Assessment%20questions/Meta/Level%201/Kaitenzushi.py)
| 16 | Double heap for the median <br> Double heaps, please don't .pop(), use heappop() | - Use heappop and don't use pop, please! <br> - Always heappush first and then heappop while adding <br> - Keep a bal variable <br> - for lazy removal, maintain a HashMap <br> - call make_top_ready before accessing the top element to guarantee you are using a valid number from the heap | [Sliding Window Median](./Heaps/Sliding%20Window%20Median.py) <br> [The Number of the Smallest Unoccupied Chair](./Heaps/The%20Number%20of%20the%20Smallest%20Unoccupied%20Chair.py)
| 17 | mid = (left+right) // 2 -> Left mid for even cases <br> mid = (left+right+1)//2 -> Right mid for even cases | - Main edge case to consider for these problems is with two elements having same values <br> - Also consider the case for empty array | [bisect_left_right](./Binary%20Search/bisect_left_right.py)
| 18 | Circular linked list insertion, insert at the drop test |  - Test cases I considered were good <br> - No list, 1 element, insert at the end | [Insert into a Sorted Circular LL](./Linked%20Lists/Insert%20into%20a%20Sorted%20Circular%20Linked%20List.py)
| 19 | When updating both next and previous of a node for a circular linked list, <br> iterate with curr and prev pointer, and create the links one way. <br> Don't complicate by creating both links for the node. <br> Create one link for each prev and curr | - In this question, I had to create a DLL from a BST <br> - My approach was correct, thinking of inorder <br> - I messed up by building both link for a node, which complicated things <br> - Instead maintaining a prev and a curr, and updating one link each pointer was way too easy <br> - Think about curr and prev when building two way, don't complicate by building both links for each node | [Convert Binary Tree to Sorted Doubly Linked List](./BST%20problems/Convert%20Binary%20Search%20Tree%20to%20Sorted%20Doubly%20Linked%20List.py)

## Patterns in problems you just need to know

| # | Summary | Comments | References |
|---|---------|----------|------------|
| 1 | Getting the next permutation of a string | - Start from the back of the string to get the char which is not in increasing order <br> - Find the character to the right of it which is just greater than that character <br> - Swap these two <br> - Reverse all the characters after the char we just found not in increasing order to start from the start | [Next Permutation](./String%20Manipulations/Next%20Permutation.py)
| 2 | Maximum brackets that can be balanced with one swap is 2 | - Example, ]][[ -> [][] <br> - Minimum swaps needed would be number of math.ceil(mismatches/2) | [Minimum Number of Swaps to Make the String Balanced](./String%20Manipulations/Minimum%20Number%20of%20Swaps%20to%20Make%20the%20String%20Balanced.py)
| 3 | Interesting iterative solution as well as binary search | - Iterative solution: if num > k, then k is the ans. Else increment k. <br> - Binary search: val - (i+1) gives the total number of missing numbers before that index | [kth missing positive number](./Binary%20Search/kth%20missing%20positive%20number.py)

