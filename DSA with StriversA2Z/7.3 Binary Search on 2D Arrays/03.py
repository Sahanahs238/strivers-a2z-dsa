def findtarget(mat,target):
    n = len(mat)
    m = len(mat[0])
    row = 0
    col = m-1
    while row < n and col >= 0:
        if mat[row][col]==target:
            return True
        elif mat[row][col]<target:
            row+=1
        else:
            col-=1
    return False
mat = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
target = 20
print(findtarget(mat,target))