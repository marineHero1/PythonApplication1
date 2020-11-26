#剑指 Offer 42. 连续子数组的最大和

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1=0
        sum1=0
        flag=0
        for i in nums:
            if(sum1+i>0):
                flag=1
                sum1+=i
                max1=max(sum1,max1)
            else:
                sum1=0
        if(flag==0):
            return max(nums)
        return max1