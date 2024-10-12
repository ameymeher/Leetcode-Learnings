"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        """
        Assumptions:
        1. Non descending order - 1 1 2 3 3
        2. Linked list, head is given
        3. head might be NULL, in that case create a circular linked list
        4. Insert anywhere in the case, 1 1 2, if inserting 1
        5. While inserting, create a node and insert that nodes reference in the list 
        6. Head might not be pointing to the minimum value


        Test cases:
        1. 1 1 2 2, insert 3
        2. Null head, insert the element and refer itself - Done
        3. 1, insert 2 - Done
        """

        if not head:
            node = Node(insertVal)
            node.next = node
            return node

        prev = head
        curr = head.next

        while True:
            if prev.val <= insertVal <= curr.val or (
                prev.val > curr.val and (insertVal >= prev.val or insertVal <= curr.val)
            ):
                prev.next = Node(insertVal,curr)
                return head

            prev = curr
            curr = curr.next

            if prev == head:
                prev.next = Node(insertVal,curr)
                return head