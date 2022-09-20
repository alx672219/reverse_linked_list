from typing import Optional
from typing import ListNode
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr:
            next_temp = curr.next   # Remember next node
            curr.next = prev   # REVERSE! None, first time round.
            prev = curr   # Used in the next iteration.
            curr = next_temp   # Move to next node.
            
        return prev