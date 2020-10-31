# 亲密字符串
 
class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        lengA=len(A)
        lengB=len(B)
        if(lengA!=lengB):
            return False
        flags=[]
        flag=0
        
        for i in range(lengA):
            if flag>2:
                return False
            if A[i]!=B[i]:
                flags.append([A[i],B[i]])
                flag+=1

        if(flag==0):
            set1=set(A)
            if(len(set1)!=lengA):
                return True
            else:
                return False
        elif(flag==1):
            return False
        else:
            if flags[0]==flags[1][::-1]:
                return True
            else:
                return False

#test=Solution()
#res=test.buddyStrings("ab","ba")
#print(res)