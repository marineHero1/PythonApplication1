#最长公共前缀
'''
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。
'''
#0(n**2)
class Solution(object):
    def longestCommonPrefix(self, strs):
        i=0
        res=""
        if(strs==[]):
            return res
        while(i<len(strs[0])):
            #假设非空，res不断变长，发现不同就返回前一个res
            j=1
            res=strs[0][:i+1]
            while(j<len(strs)):
                if(strs[j][:i+1]!=res):
                    return res[:i]
                j+=1
            i+=1
        #循环做完依旧没有返回，说明每个字符串都相等，返回第一个
        return strs[0]

'''测试
test=Solution()
res=test.longestCommonPrefix(["flower","flow","flight"])
print(res)
'''