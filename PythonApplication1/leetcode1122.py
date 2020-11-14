#1122. 数组的相对排序

class Solution(object):
    def relativeSortArray(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        dic=dict()
        res=[]
        res2=[]
        for i in range(len(arr1)):
            if(arr1[i] not in arr2):
                res2.append(arr1[i])
            elif(arr1[i] not in dic):
                dic[arr1[i]]=1
            else:
                dic[arr1[i]]+=1
        for j in arr2:
            res+=dic[j]*[j]
        return res+sorted(res2)