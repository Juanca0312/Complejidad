# Desarrolle aqui su solución (sientase libre de usar mas cajas de código si lo requiere)
adj = [ [4, 1],
        [0, 5],
        [4, 3, 5],
        [2, 4],
        [0, 2, 3, 5],
        [1, 4, 2]]

visited = [False]*len(adj)
colors = [None]*len(adj)


def bfs(v):
    visited[v] = True
    colors[v] = "Black"
    for u in adj[v]:
        if visited[u] == False:
            visited[u] = True
            colors[u] = "White"


negros = 0
sol = []
queue = []
for i in range(len(adj)):
    queue.append(i)
for inicios in range(len(adj)):
    negrosvisi = 0
    for v in queue:
        if visited[v] == False:
            negrosvisi+=1
            bfs(v)
    print(negrosvisi)
    if negrosvisi > negros:
        negros = negrosvisi
        sol = colors

    x = queue.pop(0)
    queue.append(x)
    visited = [False]*len(adj)
    colors = [None]*len(adj)   
    
print(negros)
print(sol)