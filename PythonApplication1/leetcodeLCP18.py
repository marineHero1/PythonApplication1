#LCP 18. 早餐组合
class Solution(object):
    def breakfastNumber(self, staple, drinks, x):
        #双指针
        staple=sorted(staple)
        drinks=sorted(drinks)
        leng1=len(staple)
        j=len(drinks)-1
        i=0
        res=0
        while(i<leng1 and j>=0):
            if staple[i]+drinks[j]<=x:
                res+=j+1
                i+=1
            else:
                j-=1
        return res % 1000000007