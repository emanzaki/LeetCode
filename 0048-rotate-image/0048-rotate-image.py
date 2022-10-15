class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        z = len(matrix)
        arr = []
        for i in range(z):
            arr = []
            for j in range(z):
                arr.append(matrix[-j-1][i])
            matrix.insert(0, arr)
        for i in range(z):
            del matrix[-1]
        matrix.reverse()
                
        """
        Do not return anything, modify matrix in-place instead.
        """
        