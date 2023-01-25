class Solution:
    #def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
    def matrixReshape(self, mat, r, c):
        flatten = []
        new_mat = []
        for row in mat:
            for num in row:
                flatten.append(num)
                
        if r * c != len(flatten):   # when given parameters is NOT possible and legal
            return mat
        else:
            for row_index in range(r):
                new_mat.append(flatten[row_index * c : row_index * c + c])
            return new_mat

mat = [[0,  1,  2,  3],[4,  5,  6,  7],[8,  9,  10, 11]]
r = 2
c = 6
Solution().matrixReshape(mat,r,c)