#389. 找不同
#排序找
class Solution(object):
    def findTheDifference(self, s, t):
        s=sorted(s)
        s+='1'
        t=sorted(t)
        for i,j in zip(s,t):
            if(i!=j):
                return j

#异或法
#ord字符转ASCII，chr是ASCII转字符。
class Solution(object):
    def findTheDifference(self, s, t):
        res=0
        for i in s:
            res ^= ord(i)
        for j in t:
            res ^= ord(j)
        return chr(res)