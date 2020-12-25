#455. 分发饼干

#排序+双指针
class Solution(object):
    def findContentChildren(self, g, s):
        i=0
        j=0
        g=sorted(g)
        s=sorted(s)
        while(j<len(s) and i<len(g)):
            if g[i]<=s[j]:
                i+=1
                j+=1
            else:
                j+=1
        return i