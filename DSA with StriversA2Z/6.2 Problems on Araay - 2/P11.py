def setmatrixzero(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    newZero = False
    for r in range(rows):
        for c in range(cols):
            if matrix[r][c]==0:
                matrix[0][c]=0
                if r>0:
                    matrix[r][0]=0
                else:
                    newZero = True
    for r in range(1,rows):
        for c in range(1,cols):
            if matrix[0][c]==0 or matrix[r][0]==0:
                matrix[r][c]=0
    if matrix[0][0]==0:
        for r in range(rows):
            matrix[r][0] = 0
    if newZero:
        for c in range(cols):
            matrix[0][c]=0
r_count = int(input("Enter number of rows: "))
print("Enter each row elements separated by space:")
matrix = [list(map(int, input().split())) for _ in range(r_count)]

setmatrixzero(matrix)
print("Modified Matrix:")
for row in matrix:
    print(row)