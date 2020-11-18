#134. 加油站

#low
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        leng=len(gas)
        if(sum(gas)<sum(cost)):
            return -1

        d=[]
        for i,j in zip(gas,cost):
            d.append(i-j)
        max1=max(d)
        start=d.index(max1)

        d=d*2
        i=start
        flag=0
        while(flag<leng):
            sum1=d[i]
            for k in range(i+1,i+leng):
                sum1+=d[k]
                if(sum1<0):
                    break
            if(sum1>=0):
                return i-leng if i==leng else i
            flag+=1
            i+=1
        return -1

#low2
class Solution2(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        leng=len(gas)
        if(sum(gas)<sum(cost)):
            return -1
        d=[]
        for i,j in zip(gas,cost):
            d.append(i-j)
        d=d*2
        print(d)
        i=0
        while(i<leng):
            if(d[i]>=0):
                sum1=d[i]
            else:
                i+=1
                continue
            for k in range(i+1,i+leng):
                sum1+=d[k]
                if(sum1<0):
                    break
            if(sum1>=0):
                return i-leng if i==leng else i
            i+=1
        return -1