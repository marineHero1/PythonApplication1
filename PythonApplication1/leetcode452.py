#452. 用最少数量的箭引爆气球
#思路：按point最大值排序，根据第一个节点的max1作为第一个箭，依次和后面的point的mini进行比较
#如果max1>=mini说明可以多响,检查下一个point，如果max1<mini需要使用新箭max2
class Solution(object):
    def findMinArrowShots(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        leng=len(points)
        if leng==1:
            return 1
        if leng==0:
            return 0
        points=sorted(points,key=lambda i:i[1])
        arrow=points[0][1]
        count=1
        for i in range(1,leng):
            if(arrow<points[i][0]):
                arrow=points[i][1]
                count+=1
        return count

