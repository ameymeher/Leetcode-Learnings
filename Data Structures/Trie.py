class Trie:

    def __init__(self,**kwargs):
        self.trie = {}
        words = kwargs.get('words',None)
        if words:
            for word in words:
                self.insert(word)

    # Insert a word into the trie.
    def insert(self, word: str) -> None:
        curr_trie = self.trie
        for i,c in enumerate(word):
            if c not in curr_trie:
                curr_trie[c] = {}
            curr_trie = curr_trie[c]
        curr_trie['*'] = '*' 

    # Returns if the word is in the trie.
    def search(self, word: str) -> bool:
        curr_trie = self.trie
        for c in word:
            if c in curr_trie:
                curr_trie = curr_trie[c]
            else:
                return False
        if '*' in curr_trie:
            return True
        return False

    # Returns if there is any word in the trie that starts with the given prefix.
    def startsWith(self, prefix: str) -> bool:
        curr_trie = self.trie
        for c in prefix:
            if c in curr_trie:
                curr_trie = curr_trie[c]
            else:
                return False
        return True
    
    def __repr__(self):
        return str(self.trie)
    
# Example
words = ['hello','world','he','hell']
trie = Trie(words=words)
print(trie)