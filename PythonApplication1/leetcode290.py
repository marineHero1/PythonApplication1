#290. 单词规律
class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        lst=s.split(' ')
        if(len(pattern)!=len(lst)):
            return False
        pattern2=""
        dic={}
        k=0
        for i in lst:
            if i not in dic:
                dic[i]=pattern[k]
                pattern2+=pattern[k]
            else:
                pattern2+=dic[i]
            k+=1
        if(len(set(dic.values()))!=len(dic)):
                return False
        return pattern2==pattern
