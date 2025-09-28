#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool: # type: ignore
        slow=head
        fast=head
        while fast:
            slow=slow.next
            if fast.next==None:
                return False
            else:
                fast=fast.next
                if fast.next==None:
                    return False
                else:
                    fast=fast.next
            if slow==fast:
                return True