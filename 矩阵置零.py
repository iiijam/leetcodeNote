class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rowLength = len(matrix[0])
        columnLength = len(matrix)
        rowInfo = [False for i in range(rowLength)]
        columnInfo = [False for i in range(columnLength)]
        for column in range(columnLength):
            for row in range(rowLength):
                item = matrix[column][row]
                if item == 0:
                    rowInfo[row] = True
                    columnInfo[column] = True

        for columnPosition in range(columnLength):
            if columnInfo[columnPosition] == True:
                for rowPosition in range(rowLength):
                    matrix[columnPosition][rowPosition] = 0
            for rowPosition in range(rowLength):
                if rowInfo[rowPosition] == True:
                    matrix[columnPosition][rowPosition] = 0
