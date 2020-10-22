ady = {
    "E1" : ["E2", "E4", "E5"],
    "E2" : ["E1", "E3"],
    "E3" : ["E2", "E4", "E6"],
    "E4" : ["E1", "E3", "E5", "E6"],
    "E5" : ["E1", "E4", "E6"],
    "E6" : ["E3", "E4", "E5"]
}

visited = {
    "E1" : False,
    "E2" : False,
    "E3" : False,
    "E4" : False,
    "E5" : False,
    "E6" : False
}

visited["E1"] = True




def bfs():
    queue = []
    queue.append("E1")
    while queue:
        u = queue.pop(0)
        print(u)
        for v in ady[u]:
            if visited[v] == False:
                visited[v] = True
                queue.append(v)
    

bfs()

visited = {
    "E1" : False,
    "E2" : False,
    "E3" : False,
    "E4" : False,
    "E5" : False,
    "E6" : False
}

print("Se viene el dfs mano")
print("")

def dfs(u):
    visited[u] = True
    print(u)
    for v in ady[u]:
        if visited[v] is not True:    
            dfs(v)

dfs("E1")