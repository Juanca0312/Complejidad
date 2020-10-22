
n, m = [int(x) for x in input().split()]
mat = [[] for x in range(n)]

for i in range(n):
    mat[i] = list(input())
visited = [[False for y in range(m)] for x in range(n)]

queue = []
for i in range(n):
    for j in range(m):
        if mat[i][j] == 'A':
            queue.append((i,j))

 def bfs(x, y):
    
    
    while queue:
        coord = queue.pop()

        neighbours = []

        #maximo 4 vecinos
        neighbours.append(mat[coord(0) + 1][coord(1)])
        neighbours.append(mat[coord(0) - 1][coord(1)])
        neighbours.append(mat[coord(0) ][coord(1) + 1])
        neighbours.append(mat[coord(0) ][coord(1) - 1])

        for neighbour in neighbours:
            if(visited[neighbour])
        


#recorremos los puntos para ver si hay conexiones
for i in range(n):
    for j in range(m):
        if(visited[i][j] != True and mat[i][j] != '#' and mat[i][j]):
            bfs(i, j) 



