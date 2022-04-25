def generate(numRows: int) -> list:
    # init
    yangHuiTriangle = []
    singleRow = [1]
    # generate the specific row
    for i in range(numRows):
        yangHuiTriangle.append(singleRow[:])
        if i == 0:
            singleRow.append(1)
        else:
            newRow = [1]
            for j in range(i):
                sum = singleRow[j] + singleRow[j+1]
                newRow.append(sum)
            newRow.append(1)
            singleRow[:] = newRow[:]

    return yangHuiTriangle
