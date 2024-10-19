n = int(input())
n_list = list(map(int, input().split()))
count = 0
for i in range(n):
    num = n_list[i]
    if num != 1:
        split = False
        for i in range(2, num):
            if num % i == 0:
                split = True
                break
        if split is False:
            count += 1
print(count)