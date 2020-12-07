#861. 翻转矩阵后的得分
class Solution(object):
    def matrixScore(self, A):
        """
        :type A: List[List[int]]
        :rtype: int
        """
        sumsum=0
        m=len(A)
        n=len(A[0])
        def fun(lst):
            lst2=[]
            for i in lst:
                if(i==0):
                    lst2+=[1]
                else:
                    lst2+=[0]
            return lst2
        for i in range(len(A)):
            if A[i][0]==0:
                A[i]=fun(A[i])
        for j in range(n):
            sum2=0
            sum0=0
            sum1=0
            for i in range(m):
                if A[i][j]==1:
                    sum1+=1
                else:
                    sum0+=1
            sum2=max(sum1,sum0)
            sumsum+=sum2*2**(n-j-1)

        return sumsum