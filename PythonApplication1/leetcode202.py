#202. 快乐数

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        for j in range(6):
            strn=str(n)#数字转字符串
            lst=[int(i) for i in strn]#字符串转列表
            n=sum([i**2 for i in lst])#列表逐个平方求和，生成新的n
            if(n==1):#n为1返回快乐
                return True
        #循环结束不快乐
        return False