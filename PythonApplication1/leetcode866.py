#回文素数

#low
class Solution(object):
    def primePalindrome(self, N):
        """
        :type N: int
        :rtype: int
        """
        i=N-1
        def isprime(num):
            if(num==1):
                return False
            for k in range(2,num//2+1):
                if num%k==0:
                    return False
            return True
        while(True):
            i+=1
            strs=str(i)
            if(strs[::-1]!=strs):
                continue
            if(isprime(i)):
                return i

#high 