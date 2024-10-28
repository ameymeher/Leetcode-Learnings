from collections import defaultdict

class Solution(object):
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:


        """
        beginWord = "hit", endWord = "cog", 
        wordList = ["hot","dot","dog","lot","log","cog"]

        1. Crazy way to create the graph
        """

        wordSet = set(wordList)     #{"hot","dot","dog","lot","log","cog","hit"}
        wordSet.add(beginWord)

        if endWord not in wordSet:
            return 0

        inter_graph = defaultdict(list)
        """
        {
            *ot : ["hot","dot",],
            h*t : ["hot",],
            ho* : ["hot",],
            d*t : ["dot"],
            do* : ["dot"],
        }
        """

        for word in wordSet:
            for i in range(len(word)):
                inter_graph[word[:i] + '*' + word[i+1:]].append(word)

        visited = set([beginWord])
        queue = [(beginWord,1)]

        for word,dist in queue:

            # Termination step
            if word == endWord:
                return dist

            # Exploration step
            for i in range(len(word)):
                inter_word = word[:i] + '*' + word[i+1:]

                if inter_word not in visited:
                    for nbr in inter_graph[inter_word]:
                        if nbr not in visited:
                            visited.add(nbr)
                            queue.append((nbr,dist+1))

                    visited.add(inter_word)
                    
        return 0