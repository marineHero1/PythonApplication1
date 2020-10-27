#合并两个有序数组
'''
test=l88.Solution()
nums1=[1,2,3,0,0,0]
res=test.merge(nums1,3,[2,5,6],3)
print(nums1)
'''
#low
class Solution:
    def merge(self, nums1, m, nums2, n):
        for i in range(n):
            flag=m-1
            while(flag>=0 and nums2[i]<nums1[flag]):
                #倒序后移动，nums2中元素比nums1最后一个小nums1就向后移动
                nums1[flag+1]=nums1[flag]
                flag-=1
            #对应位置腾出来，直接放入num2对应的元素
            nums1[flag+1]=nums2[i]
            m+=1
#high
class Solution2:
    def merge(self, nums1, m, nums2, n):
        nums1[:]=sorted(nums1[:m]+nums2[:])
        

        
