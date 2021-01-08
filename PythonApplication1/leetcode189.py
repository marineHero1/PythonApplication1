#189. 旋转数组
class Solution(object):
    def rotate(self, nums, k):
        leng=len(nums)
        k=k%leng
        nums2=nums[-k:]+nums[:-k]
        for i in range(leng):
            nums[i]=nums2[i]