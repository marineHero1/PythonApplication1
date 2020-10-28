#独一无二的出现次数
'''
给你一个整数数组 arr，请你帮忙统计数组中每个数的出现次数。
如果每个数的出现次数都是独一无二的，就返回 true；否则返回 false。
'''

class Solution(object):
    def uniqueOccurrences(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        num=[0]*2001
        #将输入arr调整为[0,2000]
        arr=[1000+x for x in arr]
        #循环将arr中元素按下标放入计数列表num
        for i in arr:
            num[i]+=1
        s1=set(num)
        s1.remove(0)

        for i in num:
            if i==0:
                #如果是0不做处理
                continue
            elif i in s1:
                #如果出现在集合中，移除该元素
                s1.remove(i)
                continue
            else:
                #该元素不在集合中，说明重复出现，返回False
                return False
        #循环结束，说明没有重复出现，返回True
        return True

'''
test=Solution()
res=test.uniqueOccurrences([-3,0,1,-3,1,1,1,-3,10,0])
print(res)
'''