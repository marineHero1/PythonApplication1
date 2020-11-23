#598. 范围求和 II
#思路，记录最小的mi,ni，将其求积
class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        min1,min2=m,n

        for i in ops:
            min1=min(i[0],min1)
            min2=min(i[1],min2)

        return min1*min2