import bisect
def findcount(rows,mid):
    return bisect.bisect_right(rows,mid)

def findMedian(matrix):
    row = len(matrix)
    cols = len(matrix[0])
    low = min(row[0] for row in matrix)
    high = max(row[-1] for row in matrix)
    while low<high:
        mid = (low+high)//2
        count=0
        for r in matrix:
            count += findcount(r,mid)
        if count < (row*cols+1)//2:
            low = mid +1
        else:
            high = mid
    return low
matrix = [ [1, 4, 9], [2, 5, 6], [3, 7, 8] ] 
print(findMedian(matrix))