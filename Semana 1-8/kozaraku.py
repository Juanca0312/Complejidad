#Encuentra las componentes fuertemente conexas

adj = [[1],
    [2],
    [0,4],
    [4],
    [5],
    [3]]

trans = [[2],
    [0],
    [1],
    [5],
    [2,3],
    [4]]

visited = [False] * len(adj)

order, component = [],[]

def dfs1(v):
    visited[v] = True
    for u in adj[v]:
        if(visited[u] is not True):
            dfs1(u)
    order.append(v)



def dfs2(v):
    #REINICIA VISITED
    visited[v] = True
    component.append(v)
    for u in trans[v]:
        if(visited[u] is not True):
            dfs2(u)

for i in range(len(adj)):
    if(visited[i] is not True):
        dfs1(i)

visited = [False] * len(adj)

cont = 0

for i in range(len(adj)):
    v = order[len(adj)-1-i]
    if(visited[v] is not True):
        dfs2(v)
        cont += 1
        print(component)
        component.clear()


