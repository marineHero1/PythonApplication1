#941. 有效的山脉数组

class Solution(object):
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        flag,i=0,0
        leng=len(A)
        if(leng<=2):#小于两个元素不可能
            return False
        if(A[0]>A[1]):#第一个元素大于第二个元素不可能
            return False
        while(i<leng-1):#三个元素以上循环判断
            #flag为0爬山，为1下山
            if(A[i+1]==A[i]):#平路立即退出
                break
            if(flag==1):
                if(A[i+1]>A[i]):#下山有上坡退出
                    break
            if(flag==0):
                if(A[i+1]<A[i]):#上山有下坡开始下山
                    flag=1
                    continue
            i+=1
        if(i<leng-1 or A[i]>A[i-1]):#提前结束 或 结尾两个元素是上坡 不是山
            return False
        return True

#test=Solution()
#res=test.validMountainArray([0,3,2,1])
#print(res)