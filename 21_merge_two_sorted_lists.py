# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#############################

class Solution(object):
    # RECURSIVE METHOD FOR THIS
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
    
    # ITERATIVE APPROACH
    def mergeTwoListsIterative(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        new_list = ListNode(0)
        current = new_list

        while list1 is not None and list2 is not None:
            if list1 is None or list1.val > list2.val:
                current.next = list2
                list2 = list2.next
            else:
                current.next = list1
                list1 = list1.next
            current = current.next

        if list1 is not None:
            current.next = list1
        if list2 is not None:
            current.next = list2
        
        return new_list.next



                    

        