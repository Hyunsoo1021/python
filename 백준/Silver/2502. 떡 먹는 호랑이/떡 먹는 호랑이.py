def fibo(n):
    coa = 1
    cob = 1
    for _ in range(n-3):
        temp = coa
        coa = cob
        cob += temp
    return coa, cob

d, k = map(int, input().split())
coa, cob = fibo(d)
for i in range(1, k):
    a = i
    if (k - coa * a) % cob == 0:
        b = (k - coa * a) // cob
    else:
        continue
    print(a)
    print(b)
    break