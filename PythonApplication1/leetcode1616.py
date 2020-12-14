#1616. 分割两个字符串得到回文串
#low and 超时
class Solution(object):
    def checkPalindromeFormation(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: bool
        """
        leng=len(a)
        for i in range(leng):
            res1=a[:i]+b[i:]
            if(res1==res1[::-1]):
                return True
            res2=b[:i]+a[i:]
            if(res2==res2[::-1]):
                return True
        return False

#high
class Solution(object):
    def checkPalindromeFormation(self, a, b):
        def fun(a,b):
            i=0
            j=len(a)-1
            while(i<j and a[i]==b[j]):
                i+=1
                j-=1
            if(i>=j):
                #超过中间位置直接为回文
                return True
           #相同位置结束，判断i或j进行分割是不是回文
            res1=a[i:j+1]
            res2=b[i:j+1]
            if(res1==res1[::-1] or res2==res2[::-1]):
                return True 
        if fun(a,b):
            return True
        if fun(b,a):
            return True
        if(a==a[::-1] or b==b[::-1]):
            return True
        return False

