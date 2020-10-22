import math
n = int(input())

adj = [[] for i in range(n)]
#amigos
for i in range(n):
    aux=list(map(int, input().split()))
    adj[i].extend(aux[1:])

#casos
t=int(input())

visited = [False] * n
d = [math.inf]*n #usamos matriz de distancias para ver que dia se visito mas
def bfs(test):

    d[test] = 0
    queue = []
    queue.append(test)
    while queue:
        u = queue.pop(0)
        for v in adj[u]:
            if(visited[v] == False):
                visited[v] = True
                d[v] = d[u] + 1
                queue.append(v)


for i in range(t):
    visited = [False] * n
    d = [math.inf]*n
    test=int(input())

    if not len(adj[test]):
        print(0)
        continue

    visited[test] = True
    bfs(test)
    rep = {}
    for i in range(len(d)):
        if d[i] not in rep:
            rep[d[i]] = 1
        else:
            rep[d[i]] = rep[d[i]] + 1
    maxi = 0
    day = 0
    for r in rep:
        if(rep[r] > maxi):
            maxi = rep[r]
            day = r
    print(maxi,day)




