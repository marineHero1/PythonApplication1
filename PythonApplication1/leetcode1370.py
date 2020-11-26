#1370. 上升下降字符串

class Solution:
    def sortString(self, s):
        dic=dict()
        for i in s:
            if i not in dic:
                dic[i]=1
            else:
                dic[i]+=1
        lst=sorted(dic,key=lambda i:i[0])
        flag=1
        res=[]
        i=0
        leng=len(lst)
        while(True):
            while(i<leng):
                if(dic[lst[i]]!=0):
                    res.append(lst[i])
                    dic[lst[i]]-=1
                i+=1
            i-=1
            while(i>=0):
                if(dic[lst[i]]!=0):
                    res.append(lst[i])
                    dic[lst[i]]-=1
                i-=1
            i+=1

            if(set(dic.values())=={0}):
                break
        return ''.join(res)