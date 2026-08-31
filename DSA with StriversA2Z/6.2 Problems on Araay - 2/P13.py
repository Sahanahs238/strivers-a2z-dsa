def spiralOrder(matrix):
    left ,right = 0,len(matrix[0])
    top,bottom = 0,len(matrix)
    ans = []
    while left<right and top<bottom:
        for i in range(left,right):
            ans.append(matrix[top][i])
        top +=1
        for i in range(top,bottom):
            ans.append(matrix[i][right-1])
        right -= 1
        if not (left < right and top < bottom):
            break
                
        for i in range(right-1, left-1, -1):
            ans.append(matrix[bottom-1][i])
        bottom -= 1
            
        for i in range(bottom-1, top-1, -1):
            ans.append(matrix[i][left])
        left += 1
            
    return ans
r_count = int(input("Enter number of rows: "))
print("Enter each row elements separated by space:")
matrix = [list(map(int, input().split())) for _ in range(r_count)]
result = spiralOrder(matrix)
print("Spiral Order Result:")
print(result)