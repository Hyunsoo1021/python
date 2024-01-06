n = int(input())
n_list = list(map(int, input().split()))
cur_max = 0
whole_max = 0
for i in range(len(n_list)):
    if i == 0:
        whole_max = n_list[i]
        cur_max = whole_max
    else:
        cur_max = max(n_list[i], n_list[i] + cur_max)
        if cur_max > whole_max:
            whole_max = cur_max
print(whole_max)