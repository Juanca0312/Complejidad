#Dado un conjunto de elementos, cada uno tiene un valor y un peso.
#Cual es el maximo valor que puedes obtener usando como maximo un peso de W?
#PD: no realizar calculos nuevamente. Guardar respuestas parciales a problemas

n, W = map(int, input().split())
v, w = [0] * n, [0] * n

for i in range(n):
    w[i], v[i] = map(int, input().split())

res = [[-1 for x in range(W+1)] for j in range(n)]


inf = 10**18

def solve(i, p):
    if p > W: return -inf
    if i == n: return 0
    if res[i][p] != -1:
        return res[i][p]
    ans = max(solve(i+1, p + w[i]) + v[i], solve(i+1, p))
    res[i][p] = ans
    return ans

print(solve(0,0))