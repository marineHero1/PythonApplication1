#49. 字母异位词分组

class Solution(object):
    def groupAnagrams(self, strs):
        set1=set()
        dic=dict()
        flag=0
        res=[]
        for i in strs:
            str1="".join(sorted(i))
            if str1 not in dic:
                dic[str1]=flag
                flag+=1
                res.append([])
            res[dic[str1]]+=[i]
        return res
