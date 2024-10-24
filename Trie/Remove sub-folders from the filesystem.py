class Trie:

    def __init__(self):
        self.trie = {}
        self.ans = []

    def insert(self,filesystem):
        if not filesystem and filesystem[0] =='':
            return

        curr = self.trie
        for folder in filesystem:
            if '*' in curr:
                return
            if folder not in curr:
                curr[folder] = {}
            curr = curr[folder]
        curr['*'] = '*'

    def get_folders(self,curr,curr_trie):

        if '*' in curr_trie:
            self.ans.append(curr)
            return

        for k,val in curr_trie.items():
            self.get_folders(curr + '/' + k,val)
            
class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        
        t = Trie()
        for file in folder:
            files = file.split('/')
            t.insert(files[1:])
        
        t.get_folders('',t.trie)

        return t.ans