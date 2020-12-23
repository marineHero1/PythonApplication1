#387. 字符串中的第一个唯一字符
#low
class Solution(object):
    def firstUniqChar(self, s):
        leng=len(s)
        for i in range(leng):
            if s[i] not in s[:i] and s[i] not in s[i+1:]:
                return i
        return -1

#high
class Solution:
    def firstUniqChar(self, s):
        a=collections.defaultdict(int)
        for i in s:
            a[i]+=1
        if 1 not in a.values():
            return -1
        for i,j in a.items():
            if j==1:
                return s.index(i)