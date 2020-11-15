#402. 移掉K位数字

#low
class Solution(object):
    def removeKdigits(self, num, k):
        lst=list(num)
        res=lst
        leng=len(lst)
        i=1
        flag=0
        if(leng==k):
            return "0"
        while(i<len(lst) and k>0):
            flag+=1
            while lst[i]<lst[i-1] and i>0 and k>0:
                lst=lst[:i-1]+lst[i:]
                k-=1
                i-=1
            i+=1
        print(flag)
        if(k>0):
            return str(int(''.join(lst[:-k])))
        return str(int(''.join(lst)))
        
#high
class Solution(object):
    def removeKdigits(self, num, k):
        stack=[]
        res_len=len(num)-k
        if(res_len==0):
            return "0"
        for i in num:
            while(k and stack and stack[-1]>i):
                stack=stack[:-1]
                k-=1
            stack.append(i)
        if(k>0):
            return str(int("".join(stack[:-k])))
        return str(int("".join(stack)))
        