# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeLists(self,list1,list2):
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

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        if len(lists)<=0:
            return None
        while len(lists)>1:
            merged_lists = []
            for i in range(0,len(lists),2):
                if i<len(lists)-1:
                    merged_lists.append(self.mergeLists(lists[i],lists[i+1]))
                else:
                    merged_lists.append(self.mergeLists(lists[i],None))
            lists = merged_lists
        return lists[0]

#https://leetcode.com/problems/merge-k-sorted-lists/description/

        