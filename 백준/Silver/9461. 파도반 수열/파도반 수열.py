t = int(input())
for _ in range(t):
    n = int(input())
    n_list = [0, 1, 1, 1]
    for i in range(4, n+1):
        n_list.append(n_list[i-3] + n_list[i-2])
    print(n_list[-1])