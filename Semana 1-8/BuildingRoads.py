
import resource, sys
resource.setrlimit(resource.RLIMIT_STACK, (2**29, -1))
sys.setrecursionlimit(10**7)

n, m = [int(x) for x in input().split()]
vs = [[] for x in range(n)]
for i in range(m):
    a, b = [int(x) for x in input().split()]
    ## Resto 1 para indexar el grafo desde 0
    a -= 1
    b -= 1
    vs[a].append(b)
    vs[b].append(a)



n = len(vs)
vis = [False] * n
rep = []

def dfs(v): 
    vis[v] = True
    for e in vs[v]:
        if not vis[e]:
            dfs(e)

### Recorro todos los nodos
### Tiro un DFS cada vez que encuentro un nodo no visitado
for i in range(n):
    if not vis[i]:
        #Tomo este nodo como representante de su comp.
        rep.append(i)
        dfs(i) 


### Imprimo el resultado
print(len(rep)-1)
for i in range(len(rep)-1):
	print(rep[i]+1, rep[i+1]+1)