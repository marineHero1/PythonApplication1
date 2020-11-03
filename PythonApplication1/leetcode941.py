#941. 有效的山脉数组

class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        flag,i=0,0
        leng=len(A)
        if(leng<=2):
            return False
        if(A[0]>A[1]):
            return False
        while(i<leng-1):
            if(flag==1):
                if(A[i+1]>=A[i]):
                    break
            if(flag==0):
                if(A[i+1]<A[i]):
                    flag=1
                    continue
            i+=1
        if(i<leng-1 or A[i]>=A[i-1]):
            return False
        return True

#test=Solution()
#res=test.validMountainArray([0,3,2,1])
#print(res)