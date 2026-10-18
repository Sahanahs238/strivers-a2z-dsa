def findPath(grid):
    n =len(grid)
    res =[]
    visited = [[False]*n for i in range(n)]
    def backtrack(r,c,path):
        if r == n-1 and c==n-1 :
            res.append(path)
            return
        visited[r][c]=True
        directions = [
                (1,0,"D"),
                (0,-1,"L"),
                (0,1,"R"),
                (-1,0,"U")]
        for dr,dc,move in directions:
            nr = r+dr
            nc = c+dc
            if 0<=nr<n and 0<=nc<n and grid[nr][nc]==1 and not visited[nr][nc]:
                backtrack(nr,nc,path+move)
        visited[r][c]=False
    if n>0 and grid[0][0]==1:
        backtrack(0,0,"")
    return res
grid = [ [1, 0, 0, 0] , [1, 1, 0, 1], [1, 1, 0, 0], [0, 1, 1, 1] ]
print(findPath(grid))
    
        

