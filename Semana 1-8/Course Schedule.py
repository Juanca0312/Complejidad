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


#toposort
visited = [int(0)] * n
topo = []
cycle = []


def dfs(v):
    visited[v] = 1
    for e in adj[v]:
        if visited[e] == 0:
            dfs(e)
        elif visited[e] == 1:
            cycle.append("TuBailarina77")
    topo.append(v)
    visited[v] = 2

for i in range(n):
    if(visited[i] != 2):
        dfs(i)

topo.reverse()
for i in range(len(topo)):
    topo[i] = topo[i] + 1

if len(cycle) > 0 or len(topo) == 0:
    print("IMPOSSIBLE")
else:
    for i in range(len(topo)):
        print(topo[i], end=" ", sep=" ")
