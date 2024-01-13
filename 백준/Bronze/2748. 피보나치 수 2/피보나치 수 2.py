fibo_list = dict()

n = int(input())

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    if n in fibo_list:
        return fibo_list[n]
    else:
        t = fibonacci(n-1) + fibonacci(n-2)
        fibo_list[n] = t
        return t


print(fibonacci(n))