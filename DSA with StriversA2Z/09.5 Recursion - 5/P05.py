def graphColoring(edges, m, n):
    color = [0] * n

    def isSafe(node, c):
        for u, v in edges:
            if node == u and color[v] == c:
                return False
            if node == v and color[u] == c:
                return False
        return True

    def solve(node):
        if node == n:
            return True

        for c in range(1, m + 1):
            if isSafe(node, c):
                color[node] = c

                if solve(node + 1):
                    return True

                color[node] = 0

        return False

    return solve(0)
n = 4
m = 3
edges = [ (0, 1) , (1, 2) , (2, 3) , (3, 0) , (0, 2) ]
print(graphColoring(edges,m,n))