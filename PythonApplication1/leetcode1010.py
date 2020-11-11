#1010. 总持续时间可被 60 整除的歌曲
class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        """
        lst=[0]*60
        sum1=0
        for i in time:
            lst[i%60]+=1
        for j in range(1,30):
            sum1+=lst[j]*lst[60-j]
        sum1+=lst[0]*(lst[0]-1)/2
        if(lst[30]>1):
            sum1+=lst[30]*(lst[30]-1)/2
        return sum1