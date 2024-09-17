def euclidDistance(coords, index):
    return coords[index] + coords[index+1]

#find top left [x,y] visible
def getTopLeftCoord(match):
    columnVA = match["visible_area"]
    topLeft = [100,100]
    topLeftRow = 0
    rowNum = 0
    for row in columnVA:
        for i in range (4):
            if euclidDistance(row, i*2) < sum(topLeft):
                topLeft[0] = row[i*2]
                topLeft[1] = row[i*2 + 1]
                topLeftRow = rowNum
        rowNum+=1
    return topLeft, topLeftRow

#find top right [x,y] visible
def getBottomRightCoord(match):
    columnVA = match["visible_area"]
    bottomRight = [0,0]
    bottomRightRow = 0
    rowNum = 0
    for row in columnVA:
        for i in range (4):
            if euclidDistance(row, i*2) > sum(bottomRight):
                bottomRight[0] = row[i*2]
                bottomRight[1] = row[i*2 + 1]
                bottomRightRow = rowNum
        rowNum+=1
    return bottomRight, bottomRightRow