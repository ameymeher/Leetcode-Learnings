"""
Given a binary tree root and a linked list with head as the first node. 

Return True if all the elements in the linked list starting from the head correspond to some downward path connected in the binary tree otherwise return False.

In this context downward path means a path that starts at some node and goes downwards.

Linked List in Binary Tree
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        
        """
        1 4 1 2
        """

        def build_lps(head):

            lps = [0] # This will be an array of integers
            arr = [head] # Easier to roam in the linked list for prev_lps
            prev_lps = 0
            curr = head.next

            while curr:
                if  arr[prev_lps].val == curr.val:
                    lps.append(prev_lps+1)
                    prev_lps+=1
                    arr.append(curr)
                    curr = curr.next
                else:
                    if prev_lps == 0:
                        lps.append(0)
                        arr.append(curr)
                        curr = curr.next
                    else:
                        prev_lps = lps[prev_lps-1]

            return lps,arr


        def check(root,i):
            nonlocal lps, arr

            if not root:
                return False

            while i > 0 and root.val != arr[i].val:
                i = lps[i-1]

            if root.val == arr[i].val:
                i+=1

            if i == len(arr):
                return True

            return check(root.left,i) or check(root.right,i)
            
        lps,arr = build_lps(head)
        
        return check(root,0)


"""
In DFS way
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        
        def check(root,head):
            if not root:
                return False

            ans = False
            if root.val == head.val:
                ans = dfs(root.left,head.next) or dfs(root.right, head.next)
            
            if ans:
                return True
            else:
                return check(root.left,head) or check(root.right,head)

        def dfs(root,head):
            if not head:
                return True
            
            if not root:
                return False

            if root.val != head.val:
                return False

            return dfs(root.left,head.next) or dfs(root.right,head.next)

        return check(root,head)