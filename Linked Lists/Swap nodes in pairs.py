"""
1. Always see which all links you would need to update
2. Here, there were 3 links to update.
3. Therefore, would require 3 pointers to keep track of the previous, current and the next node.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head

        sec_prev = None
        prev = head #3
        curr = head.next #4

        new_head = curr

        while prev and curr:
            prev.next = curr.next
            curr.next = prev
            if sec_prev:
                sec_prev.next = curr
            sec_prev = prev
            prev = prev.next
            curr = prev.next if prev else None

        return new_head