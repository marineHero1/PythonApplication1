#738. 单调递增的数字
#low
class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """
        #极端情况1335 1332 66881 113355771
        #        1333 1299 66799 113355699
        leng=len(str(N))
        str1=str(N)
        str1+='9'
        res=""
        res2=""
        res3=""
        flag=0
        a1=0
        for i in range(leng):
            if str1[i]==str1[i+1] and flag==0:
                res2 = res2 + str(int(str1[i])-1)
                res2 += (leng-i-1)*'9'
                a1=str1[i]
                flag=1
            if str1[i]==str1[i+1] and flag==1 and str1[i]>a1:
                res3 = res3 + str(int(str1[i])-1)
                res3 += (leng-i-1)*'9'
                flag=2
            if str1[i]>str1[i+1]:
                res = res + str(int(str1[i])-1)
                res += (leng-i-1)*'9'
                break
            else:
                res+=str1[i]
                res2+=str1[i]
                res3+=str1[i]

        if res==''.join(sorted(res)):
            return int(res[:leng])
        elif res3[:leng]==''.join(sorted(res3[:leng])) and len((res3[:leng]))==leng:
            return int(res3[:leng])
        else:
            return int(res2[:leng])

#high
class Solution(object):
    def monotoneIncreasingDigits(self, N):
        leng=len(str(N))
        str1=str(N)
        str1+='9'
        res,res2= "",""
        nums=[]
        for i in range(leng):
            if str1[i]==str1[i+1]:#记录重复情况
                nums+=[i]
            if str1[i]>str1[i+1]:
                res = str1[:i] + str(int(str1[i])-1)
                res += (leng-i-1)*'9'
                break
            else:
                res+=str1[i]
        if nums:#如果有重复
            j=str1.index(str1[nums[-1]])
            res2 = str1[:j] + str(int(str1[j])-1)
            res2 += (leng-j-1)*'9'
        return int(res[:leng]) if res==''.join(sorted(res)) else int(res2[:leng])

#high-high
class Solution:
    def monotoneIncreasingDigits(self, N):
        ones = 111111111
        result = 0
        for _ in range(9):
            while result + ones > N:
                ones //= 10
            result += ones
        return result

