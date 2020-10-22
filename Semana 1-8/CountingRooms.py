
n, m = [int(x) for x in input().split()]
mat = [[] for x in range(n)]

for i in range(n):
    mat[i] = list(input())
visited = [[False for y in range(m)] for x in range(n)]

rooms = 0


def dfs(x, y):
    visited[x][y] = True
    if( y+1 < m ):
        if(visited[x][y+1] != True and mat[x][y+1] != '#'):
            dfs(x, y+1)
    if( y-1 >= 0):
        if(visited[x][y-1] != True and mat[x][y-1] != '#'):
            dfs(x, y-1)
    if(x+1 < n ):
        if(visited[x+1][y] != True and mat[x+1][y] != '#'):
            dfs(x+1, y)
    if(x-1 >= 0):
        if(visited[x-1][y] != True and mat[x-1][y] != '#'):
            dfs(x-1, y)


#recorremos los puntos para ver si hay conexiones
for i in range(n):
    for j in range(m):
        if(visited[i][j] != True and mat[i][j] != '#'):
            dfs(i, j)
            rooms += 1

print(rooms)


