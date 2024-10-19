t = int(input())
for i in range(t):
    apa = list()
    k = int(input())
    n = int(input())
    floor_0 = list()
    for j in range(1, n+1):
        floor_0.append(j)
    apa.append(floor_0)
    for j in range(1, k+1):
        floor_list = list()
        for k in range(n):
            ho_sum = 0
            for l in range(k+1):
                ho_sum += apa[j-1][l]
            floor_list.append(ho_sum)
        apa.append(floor_list)
    print(apa[-1][-1])