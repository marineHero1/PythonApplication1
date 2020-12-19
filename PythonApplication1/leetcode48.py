#48. 旋转图像

#主对角线翻转+水平翻转
class Solution(object):
    def rotate(self, matrix):

        leng=len(matrix)
        #主对角线翻转
        for i in range(leng):
            for j in range(i):
                matrix[i][j] ,matrix[j][i] = matrix[j][i] , matrix[i][j]
        #水平翻转
        for i in range(leng):
            for j in range(leng//2):
                matrix[i][j] ,  matrix[i][leng-j-1] = matrix[i][leng-j-1] , matrix[i][j]
        