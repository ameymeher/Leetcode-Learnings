# Linked List tips

1. After finding the middle element, if you want to halve the list, remember to set the next of the first half to None
2. Iterative reversing is better than recursive reversing of the list
3. Always consider the edge case of 1 element and 2 element, odd and even elements


5. Whenever O(1) is required with HashMap, think about HashMap + LL or DLL
6. For DLL, always have a head and a tail
7. create(val,after_node) and delete(node) function makes the implementation a lot simpler