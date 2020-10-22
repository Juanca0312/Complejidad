#import resource, sys
#resource.setrlimit(resource.RLIMIT_STACK, (2**29, -1))
#sys.setrecursionlimit(10**7)

n, m = [int(x) for x in input().split()]
adj = [[] for x in range(n)]
for i in range(m):
    a, b = [int(x) for x in input().split()]
    ## Resto 1 para indexar el grafo desde 0
    a -= 1
    b -= 1
    adj[a].append(b)

topo = []
visited = [False] * n


def dfs(v):
    visited[v] = True
    for e in adj[v]:
        if visited[e] == False:
            dfs(e)
    topo.append(v)
    visited[v] = True

dfs(0)
if not visited[n-1]:
    print("IMPOSSIBLE")
    exit()

topo.reverse()
lp = [1] * n #arreglo para ver el longest path
p = [-1] * n #padres
for v in topo:
    for e in adj[v]:
        if lp[v] + 1 > lp[e]:
            lp[e] = lp[v] + 1
            p[e] = v

path = []
v = n-1
while(v != -1):
    path.append(v)
    v = p[v]

path.reverse()
print(lp[n-1])
for x in path: print(x+1, end=' \n'[x==path[-1]])