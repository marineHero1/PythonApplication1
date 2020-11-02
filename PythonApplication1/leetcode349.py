#349. 两个数组的交集
#集合的&操作返回两个的交集
#集合的|操作返回两个的并集
class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return set(nums1) & set(nums2)

#test=Solution()
#res=test.intersection([1,2,2,1],[2,2])
#print(res)