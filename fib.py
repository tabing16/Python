def fib(n):
    a,b = 0,1
    while a < n:
        yield a
        a,b = b, a + b

for i in fib(3):
    print(i)