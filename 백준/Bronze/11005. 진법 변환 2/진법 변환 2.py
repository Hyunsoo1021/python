n, b = map(int, input().split())
ans = ""
while True:
    a = n % b
    if a >=10:
        ans = chr(a+55) + ans
    else:
        ans = str(a) + ans
    if a == n:
        break
    n //= b
print(ans)