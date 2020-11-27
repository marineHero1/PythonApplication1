#454. 四数相加 II
#题目思路：遍历四个数相加过于复杂，分两次计算两个数相加
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        N=len(A)
        lst1=[]
        dic=dict()
        lst2=[]
        res=0
        for i in A:
            for j in B:
                num=i+j
                if(num not in dic):
                    dic[num]=1
                else:
                    dic[num]+=1
        for i in C:
            for j in D:
                num=-i-j
                if(num in dic):
                    res+=dic[num]

        return res