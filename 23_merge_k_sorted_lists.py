# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        if not lists:
            return None
        
        # update lists
        lists = [list for list in lists if list is not None]

        if len(lists) == 1:
            return lists[0]

        merged_list = ListNode(0)
        # helps us process the nodes
        current = merged_list

        while lists:
            min_val = float('inf')
            min_index = -1
            
            for i in range(len(lists)):
                if lists[i].val < min_val:
                    min_val = lists[i].val
                    min_index = i
            
            if min_index == -1:
                break
            # update lists
            current.next = lists[min_index]
            current = current.next
            lists[min_index] = lists[min_index].next
               
            if lists[min_index] is None:
                lists.pop(min_index)
        
            
        return merged_list.next
   
            
        