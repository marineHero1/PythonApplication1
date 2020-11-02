#61. 旋转链表
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if(not head):#空链表返回空
            return 
        if(not head.next):#单元素链表返回本身
            return head
  
        test=head
        len=1
        while(test.next):#计算链表长度，减少循环次数
            len+=1
            test=test.next
        #计算位移次数
        k=k%len

        def fun(head):#右移一位
            if(not head.next.next):#两个元素的链表返回交换位置
                a=head.val
                b=head.next.val
                head.val=b
                head.next.val=a
                return head
            res=head
            while(head.next):
                head=head.next
                if(not head.next.next):
                    a=head.next.val
                    head.next=None
            head2=ListNode(a)
            head2.next=res
            return head2
        while(k>0):
            head=fun(head)
            k=k-1
        return head
