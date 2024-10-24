class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        ans = []
        wordDict = set(wordDict)

        def backtrack(curr,candidates):
            nonlocal ans, wordDict

            if candidates == '':
                ans.append(' '.join(curr))

            for i in range(1,len(candidates)+1):
                if candidates[:i] in wordDict:
                    curr.append(candidates[:i])
                    backtrack(curr,candidates[i:])
                    curr.pop()

        backtrack([],s)

        return ans