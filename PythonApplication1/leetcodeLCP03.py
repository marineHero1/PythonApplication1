#LCP 03. 机器人大冒险、

#low 超时
class Solution(object):
    def robot(self, command, obstacles, x, y):
        """
        :type command: str
        :type obstacles: List[List[int]]
        :type x: int
        :type y: int
        :rtype: bool
        """
        road=[]
        m,n=0,0
        command=command*int((x+y)/len(command)+1)
        
        for i in command:
            if(m==x and n==y):
                return True
            if i=='U':
                n+=1
            else:
                m+=1
            if([m,n] in obstacles):
                return False
        return False
