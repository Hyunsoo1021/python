t = int(input())
for i in range(t):
    a, b, m = map(int, input().split())
    if (m-a)<(b-m):
        print(2*(m-a)+1)
    elif (m-a)>=(b-m):
        print(2*(b-m))