class Solution:
    def isValidSudoku(self, board) -> bool:
        #init
        hashSet = {}

        for row in range(9):
            for column in range(9):
                numberKey = board[row][column]
                if numberKey != '.':
                    #calculate div
                    div = (column//3) * 3 + row//3
                    if numberKey in hashSet:
                        locationFrequency = len(hashSet[numberKey])
                        for i in range(locationFrequency):
                            existedLocation = hashSet[numberKey][i]
                            existedRow = existedLocation[0]
                            existedColumn = existedLocation[1]
                            existedDiv = existedLocation[2]
                            # judge
                            if existedRow == row or existedColumn == column or existedDiv == div:
                                return False
                                break
                            else:
                                # update location
                                if i+1 == (locationFrequency):
                                    hashSet[numberKey].append([row,column,div])
                                    break
                                else:
                                    continue
                    else:
                    # save location
                        hashSet[numberKey] = []
                        hashSet[numberKey].append([row,column,div])
        
        return True