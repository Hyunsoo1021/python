def odd_or_even(a):
    if a%2 == 0:
        return 0
    else:
        return 1

n = int(input())
a = list(map(int, input().split()))
now = odd_or_even(a[0])
count = 1
for i in range(1, n):
    if odd_or_even(a[i]) != now:
        count += 1
        now = odd_or_even(a[i])
print(count)