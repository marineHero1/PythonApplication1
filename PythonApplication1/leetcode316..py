#316. 去除重复字母
class Solution(object):
    def removeDuplicateLetters(self, s):
        leng=len(s)
        if(leng<=1):
            return s
        res=""
        i=0
        while(i<leng):
            #新来元素如果不在栈中放入
            if(s[i] not in res):
                res+=s[i]
            
            while len(res)>=2:
                #栈中有两个以上元素，比较最后一个和最后第二个，符合要求退出最后第二个元素
                if res[-2]>res[-1] and res[-2] in s[i+1:]:
                    res=res[:-2]+res[-1]
                else:
                    break
            i+=1
        return res