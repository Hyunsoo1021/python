t = int(input())
for _ in range(t):
    n = int(input())
    n_list = [-1, 1, 2, 4]
    for i in range(4, n+1):
        n_list.append(n_list[i-1] + n_list[i-2] + n_list[i-3])
    print(n_list[n])