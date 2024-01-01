# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
         # Calculate the length of the list
        list_len = 0
        temp_head = head
        while temp_head:
            list_len += 1
            temp_head = temp_head.next

        if n == list_len:
            return head.next

        index_to_remove = list_len - n

        temp_head = head
        for _ in range(index_to_remove - 1):
            temp_head = temp_head.next

        temp_head.next = temp_head.next.next

        return head

#https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/