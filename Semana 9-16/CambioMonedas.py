#Cambio de monedas
import math
n = len(d)
c = [0]*(p+1)
s = [-1] * (p+1)
for i in range(1, p+1):
    c[i], s[i] = min([(1+c[i - di], di) for di in d if i - di >= 0])

usedCoins = {}
cant = c[p]
while p > 0:
    if not s[p] in usedCoins:
        usedCoins