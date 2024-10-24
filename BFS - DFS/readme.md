# BFS DFS tips

1. Never forget to use the visited set in BFS. Especially add the nodes to the visited set before adding them to the queue.
2. If there are multiple times to do the BFS (mulitple entry points), add all the nodes to the queue and then do only one BFS.
3. For the BFS, always check the terminating condition (length calculation) and the validity check (check if the required exploration strategy is going where you want it)
4. Ensure that the visited and the queue are refreshed for each BFS
5. Ensure that you are using the new variables for the validation checks and exploration strategies.