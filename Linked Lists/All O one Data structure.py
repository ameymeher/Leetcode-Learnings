"""
1. Whenever O(1) is required with HashMap, think about HashMap + LL or DLL
2. For DLL, always have a head and a tail
3. If there's a remove operation on the DLL, create it seperately, easy to manage the code
4. Also creating a new node function would also help
"""

class Node:
    def __init__(self,freq,keys):
        self.freq = freq
        self.keys = keys

class AllOne:

    def __init__(self):
        self.words = {}
        self.head = Node(-1,set())
        self.tail = Node(-1,set())
        
        self.head.next = self.tail
        self.head.prev = None
        self.tail.prev = self.head
        self.tail.next = None
        
    def inc(self, key: str) -> None:
        
        # Get the node
        if key in self.words:
            og_node = self.words[key]

            # Creation of a new node required
            if og_node.next == self.tail or og_node.freq + 1 != og_node.next.freq:
                new_node = self.createNode(og_node.freq+1,key,og_node)
                self.words[key] = new_node
            
            # Update the existing node
            else:
                og_node.next.keys.add(key)
                self.words[key] = og_node.next

             # Update the og node
            og_node.keys.remove(key)
            if len(og_node.keys) == 0:
                self.removeNode(og_node)

        # Create a new node and insert at the beginning
        else:

            # Create a new node
            if self.head.next == self.tail or self.head.next.freq != 1:
                # Add the new node
                new_node = self.createNode(1,key,self.head)
                self.words[key] = new_node

            # Update the first node
            else:
                self.head.next.keys.add(key)
                self.words[key] = self.head.next
    

    def dec(self, key: str) -> None:

        og_node = self.words[key]

        # If the word won't exist afterwards
        if og_node.freq-1 == 0:
            og_node.keys.remove(key)
            if len(og_node.keys) == 0:
                self.removeNode(og_node)
            del self.words[key]
            return

        # Just update the previous and the current
        if og_node.freq-1 == og_node.prev.freq:
            og_node.prev.keys.add(key)
            self.words[key] = og_node.prev

        # Create a new node
        else:
            new_node = self.createNode(og_node.freq-1,key,og_node.prev)
            self.words[key] = new_node

        og_node.keys.remove(key)
        if len(og_node.keys) == 0:
            self.removeNode(og_node)
        
    def getMaxKey(self) -> str:
        if self.tail.prev == self.head:
            return ""
        return next(iter(self.tail.prev.keys),"")

    def getMinKey(self) -> str:
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.keys),"")

    def removeNode(self,node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def createNode(self,freq,key,curr):
        new_node = Node(freq,{key})
        new_node.next = curr.next
        new_node.prev = curr
        curr.next = new_node
        new_node.next.prev = new_node
        return new_node


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()