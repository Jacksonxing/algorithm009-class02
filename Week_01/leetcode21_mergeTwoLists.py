# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3_head = l3_cur = ListNode(0) #chain them to save head
        
        while l1 and l2: #assert both exist
            if l2.val < l1.val:
                l3_cur.next = l2 #build l3's node
                l2 = l2.next #this is i++ 
            else:
                l3_cur.next = l1
                l1 = l1.next     
            l3_cur = l3_cur.next #find the next to build
        if l1:
            l3_cur.next = l1 
        if l2:
            l3_cur.next = l2
        return l3_head.next