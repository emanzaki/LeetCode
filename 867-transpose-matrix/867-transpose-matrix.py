class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        arr_temp = []
        rows = len(matrix)
        columns = len(matrix[0])
        for coln in range(columns):
            arr = []
            for row in range(rows):
                arr.append(matrix[row][coln])
            arr_temp.append(arr)
        return arr_temp