from itertools import product

nE, nD=[int(k) for k in input().split()] #datos de entrada
estampUso=[1] #primer arreglo que se prueba de estampas
solu=1 #prueba de solucion incial
def maxEstamp(nE, estampUso):
    cont=set() #set para no guardar valores repetidos
    for i in range(nE):
        prod=product(estampUso, repeat=i+1)
        for j in prod: #suma de combinaciones
            conta=0
            for i in j: conta+=i
            cont.add(conta)
    cont=list(cont)
    for i in range(len(cont)-1):
        if cont[i]+1==cont[i+1]:
            continue
        else:
            return cont[i]
    return cont[-1]


for i in range(nD-1):
    prueba=solu
    solu=1
    while True:
        prueba+=1
        st2=list(estampUso)
        st2.append(prueba)
        fm=maxEstamp(nE, st2) 
        if fm>solu:
            solu=fm
        elif fm<solu:
            estampUso.append(prueba-1)
            break

print(estampUso)
print(maxEstamp(nE, estampUso))