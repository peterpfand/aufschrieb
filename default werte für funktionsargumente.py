i = 5

def fib(n=i):
    if n<2:
            return n
    else:
        return fib (n-1) +fib (n-2)
def f(L=[None]):
    if L is None:
        L = []
    L.append(42)
    return L

print(f())
print(f())
