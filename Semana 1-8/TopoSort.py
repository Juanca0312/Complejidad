#Dirigido aciclico

n, m = map(int, input().split())

adj = [[] for i in range(n)]
for i in range(m):
    x,y = map(int, input().split())
    adj[x-1].append(y-1)

#visited = [False] * n
visited = [int(0)] * n

topo = []

def dfs(v):
    visited[v] = 1
    for e in adj[v]:
        if visited[e] == 0:
            dfs(e)
        elif visited[e] == 1:
            exit() #verifica si hay ciclos
    topo.append(v)
    visited[v] = 2


topo.reverse()
print(topo)
