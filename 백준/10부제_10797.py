day = int(input())
a = list(map(int, input().split()))
count = 0
for i in range(len(a)):
    if a[i] == day:
        count += 1
print(count)
