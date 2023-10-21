a = list(map(int, input().split()))
b = list(map(int, input().split()))
asc = 0
bsc = 0
for i in range(10):
    if a[i] > b[i]:
        asc += 1
    elif a[i] < b[i]:
        bsc += 1
    else:
        pass
if asc > bsc:
    print('A')
elif asc < bsc:
    print('B')
else:
    print('D')
