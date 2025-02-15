def con_to_num(a):
    if ord(a) >= 65:
        return ord(a)-55
    else:
        return ord(a)-48

n, b = input().split()
b = int(b)
ans = 0
for i in range(len(n)):
    ans += (con_to_num(n[-i-1])*(b**i))
print(ans)
    