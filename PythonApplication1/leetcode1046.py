#1046. 最后一块石头的重量

class Solution(object):
    def lastStoneWeight(self, stones):
        leng=len(stones)
        if(leng==1):
            return stones[0]
        stones=sorted(stones)
        while(len(stones)>1):
            stones[leng-2]=stones[leng-1]-stones[leng-2]
            stones=stones[:-1]
            leng-=1
            stones=sorted(stones)
        return stones[0]
