n, x = map(int, input().split())
now = -1
for i in range(n):
    s, t = map(int, input().split())
    if (s+t) <=x and now < s:
        now = s
print(now)