from typing import Optional

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional['ListNode'], l2: Optional['ListNode']) -> Optional['ListNode']:
        def reverse(linkedlist: Optional['ListNode']) -> Optional['ListNode']:
            previous = None
            current = linkedlist
            while current:
                temporary = current.next
                current.next = previous
                previous = current
                current = temporary
            return previous

        def listtostring(linkedlist: Optional['ListNode']) -> str:
            list_char = []
            while linkedlist:
                list_char.append(linkedlist.val)
                linkedlist = linkedlist.next
            return "".join(str(char) for char in list_char)

        newl1 = listtostring(reverse(l1))
        newl2 = listtostring(reverse(l2))
        # handle empty lists
        newl1 = newl1 or "0"
        newl2 = newl2 or "0"

        total = str(int(newl1) + int(newl2))

        sumlist = None
        current = None
        for char in total:
            node = ListNode(int(char))
            if sumlist is None:
                sumlist = node
                current = node
            else:
                current.next = node
                current = current.next

        return reverse(sumlist)
