# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        result_list = ListNode(0)
        current_result = result_list

        list1_obj = list1
        list2_obj = list2

        while (list1_obj != None) and (list2_obj != None):
            if list1_obj.val <= list2_obj.val:
                current_result.next = list1_obj
                list1_obj = list1_obj.next
            else:
                current_result.next = list2_obj
                list2_obj = list2_obj.next
            current_result = current_result.next

        if list1_obj != None:
            current_result.next = list1_obj

        if list2_obj != None:
            current_result.next = list2_obj

        return result_list.next
