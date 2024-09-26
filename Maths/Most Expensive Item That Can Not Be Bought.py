"""
Based on some McChicken Nugget Theorem

after primeOne*primeTwo - primeOne - primeTwo, all numbers can be made

"""

class Solution:
    def mostExpensiveItem(self, primeOne: int, primeTwo: int) -> int:
        
        return primeOne * primeTwo - primeOne - primeTwo
    
class Solution:
    def mostExpensiveItem(self, primeOne: int, primeTwo: int) -> int:
        
        arr= [False]*(primeOne*primeTwo)

        @cache
        def mark(start):
            if start < len(arr):
                arr[start] = True
            else:
                return
            mark(start + primeOne)
            mark(start + primeTwo)

        mark(0)

        for i in range(len(arr)-1,-1,-1):
            if not arr[i]:
                return i