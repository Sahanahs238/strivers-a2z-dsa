def reversematrix(matrix):
    n =len(matrix)
    for i in range(n):
        for j in range(i+1,n):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    for i in range(n):
        matrix[i].reverse()
r_count = int(input("Enter number of rows: "))
print("Enter each row elements separated by space:")
matrix = [list(map(int, input().split())) for _ in range(r_count)]

reversematrix(matrix)
print("Modified Matrix:")
for row in matrix:
    print(row)
