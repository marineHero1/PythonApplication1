#605. 种花问题

#low
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        flowerbed=[0]+flowerbed+[0]
        leng=len(flowerbed)
        for i in range(1,leng-1):
            if flowerbed[i-1]+flowerbed[i]+flowerbed[i+1]==0:
                flowerbed[i]=1
                n-=1
        return True if n<=0 else False

#high
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        flowerbed=[0]+flowerbed+[0]
        leng=len(flowerbed)
        i=0
        while i<leng-1:
            i+=1
            if(i==leng-1):
                break
            if flowerbed[i-1]+flowerbed[i]+flowerbed[i+1]==0:
                flowerbed[i]=1
                i+=1
                n-=1
        return True if n<=0 else False