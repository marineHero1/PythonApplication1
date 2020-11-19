#283. 移动零

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        leng=len(nums)
        flag=-1
        num=0
        i=-1
        if(leng==1):
            return nums
        while(i>=-leng):#i遍历列表元素
            #flag末尾0的位置的左一位
            if(nums[i]==0 and i==flag):#如果最右元素为0，flag左移1位
                flag-=1
            elif(nums[i]==0):#如果最右的0不在flag范围内，将0移动到flag位置，i:flag位置移动
                num=nums[flag]
                nums[flag]=0
                nums[i:flag]=nums[i+1:flag]+[num]
                flag-=1
            i-=1

            

