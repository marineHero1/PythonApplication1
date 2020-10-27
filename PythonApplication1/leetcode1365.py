
class Solution:
    def smallerNumbersThanCurrent(self, nums):
        res=[]
        n=[0]*101

        for i in nums:
            n[i]+=1
        
        for j in range(len(nums)):
            res.append(sum(n[:nums[j]]))
 
        return res
'''测试，有多少小于当前数字的数字
test=Solution()
res=test.smallerNumbersThanCurrent([8,1,2,2,3])
print(res)
'''