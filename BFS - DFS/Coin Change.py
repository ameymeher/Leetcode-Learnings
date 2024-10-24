class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        visited = set([0]) #{0,1,2,3,4,5,6,7,10}
        queue = [(0,0)] #[(3,2),(6,2),(4,2),(7,2),(10,2)]

        for curr_sum, n_coins in queue:

            # Termination step
            if curr_sum > amount:
                continue
            
            if curr_sum == amount:
                return n_coins

            # Exploration step
            for val in coins:
                if curr_sum + val not in visited:
                    visited.add(curr_sum+val)
                    queue.append((curr_sum+val,n_coins+1))

        return -1