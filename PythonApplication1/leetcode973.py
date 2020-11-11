#973. 最接近原点的 K 个点

#low
class Solution(object):
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        leng=len(points)
        dic=dict()
        res=[]
        j=0
        for i in range(leng):
            dic[i]=points[i][0]**2+points[i][1]**2
        dic=sorted(dic.items(), key=lambda item:item[1])
        while(j<K):
            res.append(points[dic[j][0]])
            j+=1
        return res

#high
class Solution2:
    def kClosest(self, points, K):
        return sorted(points, key = lambda x:x[0]**2+x[1]**2)[:K]

#test=Solution2()
#res=test.kClosest([[3,3],[5,-1],[-2,4]],1)
#print(res)