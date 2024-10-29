# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#############################
# RECURSIVE METHOD FOR THIS

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        if list1.val > list2.val:
            new_list = ListNode(list2.val)
            new_list.next = self.mergeTwoLists(list1, list2.next)
        else:
            new_list = ListNode(list1.val)
            new_list.next = self.mergeTwoLists(list1.next, list2)
        
        return new_list



                    

        