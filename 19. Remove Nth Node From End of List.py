# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]: # type: ignore
        copy=head
        total_count=0
        while copy:
            total_count+=1
            copy=copy.next
        if total_count-n==0:
            return head.next
        first=head
        second=head.next
        for i in range(1,(total_count-n),1):
            first=first.next
            second=second.next
            print(i)
        print(first)
        print(second)
        first.next=second.next
        return head
