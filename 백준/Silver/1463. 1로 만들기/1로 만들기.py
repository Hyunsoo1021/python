n_list = [-1, 0, 1, 1]
n = int(input())
for i in range(4, n + 1):
    t_list = []
    if i%2 == 0:
        t_list.append(n_list[i//2] + 1)
    if i%3 == 0:
        t_list.append(n_list[i//3] + 1)
    t_list.append(n_list[i - 1] + 1)
    n_list.append(min(t_list))
if n != 1:
    print(n_list[-1])
else:
    print(0)