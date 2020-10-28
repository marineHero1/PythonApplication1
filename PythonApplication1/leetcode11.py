#盛最多水的容器

#low O(n**2)不能解决问题
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max=0
        for i in range(len(height)):
            for j in range(i+1,len(height)):
                sum=(j-i)*min(height[i],height[j])
                if(sum>max):
                    max=sum
        return max

#high 双指针法 O(n)
class Solution2(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max1=0
        i=0
        j=len(height)-1
        while(i<j):
            #i最左，j最右，逐渐向内
            sum=(j-i)*min(height[i],height[j])
            max1=max(sum,max1)
            if(height[i]<height[j]):
                i+=1
            else:
                j-=1
        return max1
'''
test=Solution()
res=test.maxArea([1,8,6,2,5,4,8,3,7])
print(res)
'''