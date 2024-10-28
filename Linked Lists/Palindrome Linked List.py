# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
1. After finding the middle element, if you want to halve the list, remember to set the next of the first half to None
2. Iterative reversing is better than recursive reversing of the list
3. Always consider the edge case of 1 element and 2 element, odd and even elements
"""
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        if not head.next:
            return True

        # Find the middle.
        prev = None
        middle = head
        fast = head

        while fast and fast.next:
            prev = middle
            middle = middle.next
            fast = fast.next.next

        if prev:
            prev.next = None

        # Reverse the second list O(N) time and O(N) space for the stack
        def reverse(node):
            if node.next is None:
                return node
            root = reverse(node.next)
            node.next.next = node
            return root

        # Iterative approach O(N) time and O(1) space
        prev = None
        while middle:
            middle.next,prev, middle = prev, middle, middle.next

        middle = prev

        # Compare
        while head and middle:
            if head.val != middle.val:
                return False
            head = head.next
            middle = middle.next

        return True