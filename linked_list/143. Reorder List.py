# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None: # type: ignore
        """
        Do not return anything, modify head in-place instead.
        """
        first=head
        while first: 
            current=first
            if current.next==None:
                break
            while current.next.next!=None:
                current=current.next
            last=current.next
            current.next=None
            tempnext=first.next
            first.next=last
            last.next=tempnext
            first=first.next.next