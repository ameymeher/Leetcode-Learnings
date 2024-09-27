"""
1. Standard dfs process
2. The main optimization is to check if the word can be formed with the characters in the board
3. If not, return False
4. If yes, then do the dfs
5. The other optimization is to check if the most occuring character is at the start or end of the word
6. If it is at the start, then reverse the word
7. This is because the most occuring character will be the first to be checked in the board
8. If it is at the end, then the dfs will be called for all the characters in the word
9. This will lead to more number of dfs calls
10. So, reversing the word will make the dfs calls less

"""

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        from collections import defaultdict

        m = len(board)
        n = len(board[0])
        
        # Optimization here unseen til now
        counter = defaultdict(int)
        for i in range(m):
            for j in range(n):
                counter[board[i][j]] += 1

        # Reversed the order if the most occuring is at the start
        if counter[word[0]] > counter[word[-1]]: 
            word = word[::-1]

        # Main optimization here, dont do the dfs if there are not adequate 
        #characters
        for char in word:
            if counter[char] == 0: 
                return False
            counter[char] -= 1

        def dfs(i,j,word):
            if not word:
                return True

            if (i < 0 or i>=m or
                    j < 0 or j>=n or
                    board[i][j]!=word[0]
            ):
                return False

            
            temp, board[i][j] = board[i][j], ''

            ans = ( dfs(i+1,j,word[1:]) or
            dfs(i,j+1,word[1:]) or
            dfs(i-1,j,word[1:]) or
            dfs(i,j-1,word[1:]) )
            
            board[i][j] = temp

            return ans

        for i in range(m):
            for j in range(n):
                if dfs(i,j,word):
                    return True

        return False