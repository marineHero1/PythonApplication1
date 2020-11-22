#242. 有效的字母异位词

#low
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        def fun(string):
            res={}
            for i in string:
                if i not in res:
                    res[i]=1
                else:
                    res[i]+=1
            return res
        return (fun(s)==fun(t))

#high
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        return (sorted(s)==sorted(t))