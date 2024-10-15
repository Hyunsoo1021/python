def f(n):
    if 2 > n:
        return n
    else:
        return f(n-1) + f(n-2)


a = input()
a = int(a)
print(f(a))