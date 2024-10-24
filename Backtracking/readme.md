# Backtracking tips

1. When the constraints are low, this is a good approach to solve the problem.
2. To optimize backtracking, we need to think about a good pruning strategy.
3. When dealing with strings, take good care of the loops. Eg. for i in range(1,len(s)+1) is a common pattern, not for i in range(1,len(s))
4. "All possible solutions" is a good hint that backtracking is a good approach.
5. For copying a 2D array ans to the global variable, use a deepcopy instead of ans.copy().
6. The backtracking function should not be complex, try to just pass the index instead of the whole candidates array.