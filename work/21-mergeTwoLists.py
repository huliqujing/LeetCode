# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        
        """
        ## 如果L1为空则返回L2，如果L2为空则返回L1
        if not (list1 and list2):
            return list1 if list1 else list2
        ## 用L1.val获取头节点的数值域
        s = Solution()
        if list1.val <= list2.val:
            list1.next = s.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = s.mergeTwoLists(list2.next, list1)
            return list2
