# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class SLinkedList:
   def __init__(self):
      self.headval = None
      
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        new_head = ListNode()
        current_new = new_head
        while list1!=None and list2!=None:
            if list1.val<=list2.val:
                current_new.next = ListNode(val=list1.val)
                current_new = current_new.next
                list1 = list1.next
            else:
                current_new.next = ListNode(val=list2.val)
                current_new = current_new.next
                list2 = list2.next
        while list1!=None:
            current_new.next = ListNode(val=list1.val)
            current_new = current_new.next
            list1 = list1.next
        while list2!=None:
            current_new.next = ListNode(val=list2.val)
            current_new = current_new.next
            list2 = list2.next

        return new_head.next
            
#https://leetcode.com/problems/merge-two-sorted-lists/description/