#509. 斐波那契数

#low 递归时间复杂O(2^n)
class Solution(object):
    def fib(self, N):   
        if(N==0):
            return 0
        if(N==1):
            return 1
        return self.fib(N-1)+self.fib(N-2)

#mid 数字记录法O(n)
class Solution(object):
    #0、1、2...N，共N+1位
    def fib(self, N):
        if(N<=1):
            return N
        s=[0]*N
        s[1]=1
        for i in range(2,N):
            s[i]=s[i-1]+s[i-2]
        return s[N-1]+s[N-2]