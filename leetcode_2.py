# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        new_list = ListNode()
        head = new_list
        while l1!=None and l2!=None:
            head.next = ListNode((l1.val+l2.val+carry)%10)
            #print(head.next)
            carry = (l1.val+l2.val+carry)//10
            l1 = l1.next
            l2 = l2.next
            head = head.next
        
        while l1:
            head.next = ListNode((l1.val+carry)%10)
            carry = (l1.val+carry)//10
            head = head.next
            l1 = l1.next
        while l2:
            head.next = ListNode((l2.val+carry)%10)
            carry = (l2.val+carry)//10
            head = head.next
            l2 = l2.next
        if carry>0:
            head.next = ListNode(carry)
        return new_list.next

#https://leetcode.com/problems/add-two-numbers/description/