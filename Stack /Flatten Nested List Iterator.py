# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

"""
Solution 1 using recursion
"""
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger],level=0):
        self.flat_list = []
        self.add_to_list(nestedList)
        self.curr = 0

    
    def add_to_list(self,nestedList):
        for i in nestedList:
            if i.isInteger():
                self.flat_list.append(i.getInteger())
            else:
                self.add_to_list(i.getList())
    
    def next(self) -> int:
        self.curr+=1
        return self.flat_list[self.curr-1]
    
    def hasNext(self) -> bool:
        if self.curr < len(self.flat_list):
            return True
        return False

"""
Solution 2 using one stack
"""
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = [i for i in reversed(nestedList)]
    
    def next(self) -> int:
        return self.stack.pop().getInteger()
    
    def hasNext(self) -> bool:
        self.makeTopInteger()
        if self.stack:
            return True
        return False

    def makeTopInteger(self):
        while self.stack and not self.stack[-1].isInteger():
            if self.stack[-1].getList():
                self.stack.extend(reversed(self.stack.pop().getList()))
            else:
                self.stack.pop()


"""
Solution 3 using two stacks by avoiding reversed
"""
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = [nestedList]
        self.curr = [0]
    
    def next(self) -> int:
        return self.stack.pop().getInteger()
    
    def hasNext(self) -> bool:
        self.makeTopInteger()
        if self.stack:
            return True
        return False

    def makeTopInteger(self):
        while self.stack and isinstance(self.stack[-1],list):
 
            if self.curr[-1] < len(self.stack[-1]):

                element_to_add = self.stack[-1][self.curr[-1]]
                self.curr[-1]+=1

                if not element_to_add.isInteger():
                    self.stack.append(element_to_add.getList())
                    self.curr.append(0)
                else:
                    self.stack.append(element_to_add)
            else:
                self.curr.pop()
                self.stack.pop()

"""
Solution 4 using generators
"""
class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.last_value = None
        self.generator = self.get_generator(nestedList)
    
    def get_generator(self,nestedList)->int:
        for element in nestedList:
            if element.isInteger():
                yield element
            else:
                yield from self.get_generator(element.getList())

    def next(self):
        value, self.last_value = self.last_value, next(self.generator,None)
        return value

    def hasNext(self):
        if not self.last_value:        
            self.last_value = next(self.generator,None)

        return self.last_value is not None