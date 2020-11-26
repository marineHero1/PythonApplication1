#164. 最大间距

class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums=sorted(nums)
        leng=len(nums)

        if(leng==1 or leng==0):
            return 0
        max1=nums[1]-nums[0]
        i=0
        for j in range(1,leng):
            max1=max(max1,nums[j]-nums[i])
            i+=1
        return max1