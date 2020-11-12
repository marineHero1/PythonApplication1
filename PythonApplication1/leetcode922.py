#922. 按奇偶排序数组 II

class Solution(object):
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """

        res=[0]*len(A)
        i=0
        k=1
        for j in A:
            if j%2==0:
                res[i]=j
                i+=2
            else:
                res[k]=j
                k+=2
        return res