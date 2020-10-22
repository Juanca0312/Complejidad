#Se busca escribir el camino mas corto de nodo 0 a nodo nodo
n, m = [int(x) for x in input().split()]
vs = [[] for x in range(n)]

for i in range(m):
    a, b = [int(x) for x in input().split()]
    ## Resto 1 para indexar el grafo desde 0
    a -= 1
    b -= 1
    vs[a].append(b)
    vs[b].append(a)

queue = []
visited = [False]*n
father = [None]*n


visited[0] = True
queue.append(0)

def bfs():
    while queue:
        u = queue.pop(0)
        for v in vs[u]:
            if(visited[v] == False):
                visited[v] = True
                father[v] = u
                queue.append(v)

    return False
bfs()


if(father[n-1] == None):
    print("IMPOSSIBLE")
else:
    path = []
    ini = n-1
    while(ini != None):
        path.append(ini+1)
        ini = father[ini]
    print(len(path))
    path.reverse()
    for i in range(len(path)):
        print(path[i], end=" ", sep="")



