import sys

def sol(x, y):
    cont = 0

    n = x
    m = y
    adj = [[] for x in range(n)]
    for i in range(n):
        adj[i] = list(input())

    visited = [[False for y in range(m)] for x in range(n)]
        
    def dfs(r, c):
        visited[r][c] = True

        if(r + 1 < n):
            if(adj[r+1][c] != '*' and visited[r+1][c] != True):
                dfs(r+1, c)
        if(r - 1 >= 0):
            if(adj[r-1][c] != '*' and visited[r-1][c] != True):
                dfs(r-1, c)
        if(c - 1 >= 0):
            if(adj[r][c-1] != '*' and visited[r][c-1] != True):
                dfs(r, c-1)
        if(c + 1< m):
            if(adj[r][c+1] != '*' and visited[r][c+1] != True):
                dfs(r, c+1)
        

        if(r + 1 < n and c + 1 < m):
            if(adj[r+1][c+1] != '*' and visited[r+1][c+1] != True):
                dfs(r+1, c+1)
        if(r - 1 >= 0 and c + 1 < m):
            if(adj[r-1][c+1] != '*' and visited[r-1][c+1] != True):
                dfs(r-1, c+1)
        if(r - 1 >= 0 and c - 1 >= 0):
            if(adj[r-1][c-1] != '*' and visited[r-1][c-1] != True):
                dfs(r-1, c-1)
        if(r + 1 < n and c - 1 >= 0):
            if(adj[r+1][c-1] != '*' and visited[r+1][c-1] != True):
                dfs(r+1, c-1)


    for i in range(n):
        for j in range(m):
            if(adj[i][j] == '@' and visited[i][j] != True): #lanzamos dfs en todos los nodos no visitados por si hay compoentes
 
                dfs(i, j)
                cont+=1

    return cont

for inp in sys.stdin: #para while(cin>>)
    x, y = inp.split()
    x = int(x)
    y = int(y)
    if (x != 0):
        print(sol(x, y))
    else:
        break