#976. 三角形的最大周长

class Solution(object):
    def largestPerimeter(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A=sorted(A)
        leng=len(A)
        sum1=0
        i=leng-3
        while(i>=0):
            if(A[i+2]>=2*A[i+1]):
                i-=1
                continue
            if(A[i+2]<A[i+1]+A[i]):
                sum1=sum(A[i:i+3])
                break
            i-=1
        return sum1