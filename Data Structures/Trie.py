class Trie:

    # Initialize data structure
    def __init__(self,**kwargs):
        self.trie = {}
        words = kwargs.get('words',None)
        if words:
            for word in words:
                self.insert(word)

    # Insert a word into the trie
    def insert(self, word: str) -> None:
        curr_trie = self.trie
        for i,c in enumerate(word):
            if c not in curr_trie:
                curr_trie[c] = {}
            curr_trie = curr_trie[c]
        curr_trie['*'] = '*' 

    # Returns if the word is in the trie
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

    # Returns if there is any word in the trie that starts with the given prefix
    def startsWith(self, prefix: str) -> bool:
        curr_trie = self.trie
        for c in prefix:
            if c in curr_trie:
                curr_trie = curr_trie[c]
            else:
                return False
        return True
    
    # Remove a word from the trie
    def remove(self,word):
        def remove_word(word,curr_trie):
            if word == '':
                if '*' in curr_trie:
                    del curr_trie['*']
                    return not curr_trie
                return False
            elif word[0] not in curr_trie:
                return False
            else:
                if remove_word(word[1:],curr_trie[word[0]]) and not curr_trie[word[0]]:
                    del curr_trie[word[0]]
                    return True
                return False
        remove_word(word,self.trie)

    # Returns the first n suggestions for a given prefix
    def first_n_suggestions(self,prefix,n):
        sgn = []

        # Go to the node which is at the end of the prefix
        curr_trie = self.trie
        for c in prefix:
            if c not in curr_trie:
                return sgn
            curr_trie = curr_trie[c]

        # Do DFS in a particular order till you get n answers
        def dfs(curr_trie,curr_word):
            nonlocal sgn,n

            if '*' in curr_trie:
                sgn.append(curr_word)

            for key in sorted(curr_trie):
                if len(sgn) == n:
                    return
                if key != '*':
                    dfs(curr_trie[key],curr_word + key)

        dfs(curr_trie,prefix)

        return sgn
        
    # Returns the trie
    def __repr__(self):
        return str(self.trie)
    
# Example

print("Creating a trie with words hello, world, he, hell, ''")
words = ['hello','world','he','hell','']
trie = Trie(words=words)

print("Trie: ",trie)
print()

print("3 suggestions for prefix he: ",trie.first_n_suggestions('he',3))
print()

print("Removing help from trie")
trie.remove('help')
print("Checking hello in trie: ",trie.search('hello'))
print("Checking world in trie: ",trie.search('world'))
print("Checking he in trie: ",trie.search('he'))
print("Checking hell in trie: ",trie.search('hell'))
print("Checking '' in trie: ",trie.search(''))
print("Checking help in trie: ",trie.search('help'))
print()

print("Removing he from trie")
trie.remove('he')
print("Checking hello in trie: ",trie.search('hello'))
print("Checking world in trie: ",trie.search('world'))
print("Checking he in trie: ",trie.search('he'))
print("Checking hell in trie: ",trie.search('hell'))
print("Checking '' in trie: ",trie.search(''))
print("Checking help in trie: ",trie.search('help'))
print()

print("Removing heyy from trie")
trie.remove('heyy')
print("Checking hello in trie: ",trie.search('hello'))
print("Checking world in trie: ",trie.search('world'))
print("Checking he in trie: ",trie.search('he'))
print("Checking hell in trie: ",trie.search('hell'))
print("Checking '' in trie: ",trie.search(''))
print("Checking help in trie: ",trie.search('help'))
print()

print("Removing hello from trie")
trie.remove('hello')
print("Checking hello in trie: ",trie.search('hello'))
print("Checking world in trie: ",trie.search('world'))
print("Checking he in trie: ",trie.search('he'))
print("Checking hell in trie: ",trie.search('hell'))
print("Checking '' in trie: ",trie.search(''))
print("Checking help in trie: ",trie.search('help'))
print()