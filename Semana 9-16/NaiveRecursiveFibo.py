#Naive recursive Fibonacci
def fiboNaive(n: int):
    if n == 0 or n == 1:
        return n
    else:
        return fiboNaive(n-1) + fiboNaive(n-2)

print(fiboNaive(10))

#Programacion dinamica fibo
def fibo(n: int):
    t = [-1]*(n+1)
    def f(n: int):
        if n < 2:
            t[0] = 0
            t[1] = 1
        else:
            f(n-1)
            t[n] = t[n-1] + t[n-2]
    f(n)
    return t[n]

print(fibo(10))