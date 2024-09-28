"""
Efficient solution for a circular deque
"""

class MyCircularDeque:

    def __init__(self, k: int):
        self.queue = [0] * k
        self.front = 0
        self.rear = -1
        self.count = 0
        self.maxSize = k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        self.front = (self.front - 1) % self.maxSize # front index decrease
        self.queue[self.front] = value
        self.count += 1
        return True

    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        self.rear = (self.rear + 1) % self.maxSize # rear index increase
        self.queue[self.rear] = value 
        self.count += 1
        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.maxSize
        self.count -= 1
        return True

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1) % self.maxSize
        self.count -= 1
        return True


    def getFront(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.queue[self.rear]

    def isEmpty(self) -> bool:
        return self.count == 0

    def isFull(self) -> bool:
        return self.count == self.maxSize


"""
Solution with a double ended linked list
"""

class Node:
    def __init__(self,val=None):
        self.val = val
        self.prev = None
        self.next = None

    def __repr__(self):
        return str(self.val)

class MyCircularDeque:

    def __init__(self, k: int):
        self.size = k
        self.head = Node()
        self.tail = Node()

        self.head.next = self.tail
        self.tail.prev = self.head

    def __repr__(self):
        curr = self.head.next
        ans = 'head->'
        while curr != self.tail:
            ans += str(curr) + '->'
            curr = curr.next

        return ans + 'tail'

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False

        self.size-=1

        node = Node(value)
        self.head.next.prev = node
        node.next = self.head.next
        node.prev = self.head
        self.head.next = node

        print(f"After inserting {value} at First: {self.__repr__()}")

        return True

        
    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False

        self.size-=1

        node = Node(value)
        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node

        print(f"After inserting {value} at Last: {self.__repr__()}")

        return True

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False

        self.size += 1

        temp = self.head.next
        self.head.next = self.head.next.next
        self.head.next.prev = self.head
        del temp

        print(f"After deleting value at First: {self.__repr__()}")

        return True
        

    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False

        self.size += 1

        temp = self.tail.prev
        self.tail.prev = self.tail.prev.prev
        self.tail.prev.next = self.tail
        del temp

        print(f"After deleting value at Last: {self.__repr__()}")

        return True
        

    def getFront(self) -> int:
        if not self.isEmpty():
            return self.head.next.val
        return -1

    def getRear(self) -> int:
        if not self.isEmpty():
            return self.tail.prev.val
        return -1

    def isEmpty(self) -> bool:
        if self.head.next == self.tail:
            return True
        return False
        
    def isFull(self) -> bool:
        if self.size==0:
            return True
        return False


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()s