MatrixColumRow = 9
matrix = []
rowMaxNumber = 0
coordinates = []
for rowNum in range(0,MatrixColumRow):
    row = list(map(int,input().split(" ")))
    matrix.append(row)

for rowNum in range(0,MatrixColumRow):

    if rowMaxNumber < max(matrix[rowNum]):
        rowMaxNumber = max(matrix[rowNum])
        coordinates = [(rowNum + 1, matrix[rowNum].index(max(matrix[rowNum]))+1)]
    if rowMaxNumber == max(matrix[rowNum]):
        coordinates.append((rowNum + 1, matrix[rowNum].index(max(matrix[rowNum]))+1))

print(rowMaxNumber)
for coordinate in coordinates:
    print(f"{coordinate[0]} {coordinate[1]}")