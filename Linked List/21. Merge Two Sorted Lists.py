# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head=ListNode()
        merged_list=ListNode()
        head=merged_list
        while(list1!=None and list2!=None):
            node=ListNode()
            if list1.val<=list2.val:
                node.val=list1.val
                merged_list.next=node
                list1=list1.next
            else:
                node.val=list2.val
                merged_list.next=node
                list2=list2.next
            merged_list=merged_list.next
        if (list1!=None):
            merged_list.next=list1
        elif (list2!=None):
            merged_list.next=list2
        return head.next