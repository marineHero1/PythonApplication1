#147. 对链表进行插入排序
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#low
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if(not head):#空节点直接返回
            return head
            
        now=ListNode(head.val)
        res=now
        while(head.next):
            head=head.next
            value=head.val
            #插入
            #insert(res,value)
            now=res
            if(not now.next):#单元素插入
                if(now.val>value):
                    now.next=ListNode(now.val)
                    now.val=value
                else:
                    now.next=ListNode(value)
                continue
            if(value<=now.val):#插入头部
                yidong=now
                now=ListNode(value)
                now.next=yidong
                res=now
                continue
                
            while(now.next):
                if value>now.next.val and not now.next.next:#插入尾部
                    now.next.next=ListNode(value)
                if value>=now.val and value<now.next.val:#插入中间
                    yidong=now.next
                    now.next=ListNode(value)
                    now.next.next=yidong
                    now=now.next
                now=now.next
        return res

#high
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if(not head):#空节点直接返回
            return head
            
        res1=[head.val]
        while(head.next):
            head=head.next
            res1.append(head.val)
        res1=sorted(res1)
        res=ListNode(1)
        now=res
        for i in res1:
            now.next=ListNode(i)
            now=now.next
        return res.next
        