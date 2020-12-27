#205. 同构字符串

class Solution(object):
    def isIsomorphic(self, s, t):
        dic=dict()
        for i,j in zip(s,t):
            if i not in dic and j in dic.values():
                return False
            elif i not in dic:
                dic[i]=j
            else:
                if(dic[i]!=j):
                    return False
        return True