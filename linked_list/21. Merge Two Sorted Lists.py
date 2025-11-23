#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]: # type: ignore
        if not list1:
            return list2
        elif not list2:
            return list1
        merged=ListNode()
        if list1.val<list2.val:
            merged.val=list1.val
            list1=list1.next
        else:
            merged.val=list2.val
            list2=list2.next
        current=merged
        while list1 and list2:
            tempnode=ListNode()
            if list1.val<list2.val:
                tempnode.val=list1.val
                current.next=tempnode
                current=tempnode
                list1=list1.next
            else:
                tempnode.val=list2.val
                current.next=tempnode
                current=tempnode
                list2=list2.next
        if list1:
            current.next=list1
        if list2:
            current.next=list2
        return merged