#860. 柠檬水找零

class Solution(object):
    def lemonadeChange(self, bills):
        """
        :type bills: List[int]
        :rtype: bool
        """
        count1=0
        count2=0
        #count3=0
        for i in bills:
            if(i==5):
                count1+=1
            elif(i==10):
                if(count1==0):
                    return False
                count2+=1
                count1-=1
            #20元处理
            else:
                if count1<=0:
                    return False
                else:
                    if count2>0:
                        count2-=1
                        count1-=1
                    elif count1>=3:
                        count1-=3
                    else:
                        return False
        return True