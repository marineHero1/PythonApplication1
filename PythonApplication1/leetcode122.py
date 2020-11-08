#122. 买卖股票的最佳时机 II

#low
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        lst=[]
        i=0
        sum1=0
        leng=len(prices)
        if(leng==1):
            return 0
        while(i<leng-1):
            lst=[prices[i]]
            if(prices[i+1]<prices[i]):
                i+=1
                continue
            while(i<leng-1 and prices[i+1]>=prices[i]):
                lst.append(prices[i+1])
                i=i+1
            sum1+=lst[-1]-lst[0]
            print(lst)
        return sum1

#high
class Solution2(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        i=0
        sum1=0
        leng=len(prices)
        while(i<leng-1):
            if(prices[i+1]>prices[i]):
                sum1+=prices[i+1]-prices[i]
            i+=1
        return sum1

#test=Solution()
#res=test.maxProfit([7,1,5,3,6,4])
#print(res)