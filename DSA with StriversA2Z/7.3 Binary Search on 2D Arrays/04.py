def findmaxincol(mat,col):
    n = len(mat)
    maxi = -1
    index =-1
    for i in range(n):
        if mat[i][col]>maxi:
            maxi = mat[i][col]
            index = i
    return index
def findmaxgrid(mat):
    n = len(mat)
    m = len(mat[0])
    low =0
    high = m-1
    while low<=high:
        mid = (low+high)//2
        row = findmaxincol(mat,mid)
        left = mat[row][mid-1] if mid -1 >=0 else float('-inf')
        right = mat[row][mid+1] if mid+1 <n else float('-inf')
        if mat[row][mid]>left and mat[row][mid]>right:
            return [row,mid]
        elif mat[row][mid]<left:
            high = mid-1
        else:
            low = mid+1
    return [-1,-1]
mat = [[1,4],[3,2]]
print(findmaxgrid(mat))