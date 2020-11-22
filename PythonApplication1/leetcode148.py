#148. 排序链表

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
            
#
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        #二分法
        nums=[]
        while(head):
            nums.append(head.val)
            head=head.next
        nums=sorted(nums)
        res=ListNode(0)
        now=res
        for i in nums:
            now.next=ListNode(i)
            now=now.next
        return res.next