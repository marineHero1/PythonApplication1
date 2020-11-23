#492. 构造矩形
class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        #合数的积,任意合数m=a*b,求出所有a\b的取值
        for i in range(int(math.sqrt(area)),area+1):
            if(area%i==0 and i>=area/i):
                return [i,area/i]