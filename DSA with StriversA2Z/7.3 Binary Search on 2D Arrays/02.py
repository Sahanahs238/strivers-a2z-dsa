def Search2Dmatrix(mat,target):
    n = len(mat)
    m = len(mat[0])
    low = 0
    high = (m*n)-1
    while low <= high:
        mid = (low+high)//2
        row = mid//m
        col = mid%m
        if mat[row][col]==target:
            return True
        elif mat[row][col] < target:
            low = mid +1
        else :
            high = mid-1
    return False
mat = [ [1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12] ]
target = 8
print(Search2Dmatrix(mat,target))
