# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        list_val=[]
        while head:
            list_val.append(head.val)
            head=head.next
        reverse=ListNode()
        reverse.val=list_val[len(list_val)-1]
        previous=reverse
        for i in range(len(list_val)-2,-1,-1):
            temp_node=ListNode()
            temp_node.val=list_val[i]
            previous.next=temp_node
            previous=temp_node
        return reverse    