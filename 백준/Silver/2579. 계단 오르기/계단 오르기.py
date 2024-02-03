n = int(input())
score_list = [0]
for _ in range(n):
    score_list.append(int(input()))
if n != 1:
    n_list_1 = [0, score_list[1], score_list[1] + score_list[2]]
    n_list_2 = [0, 0, score_list[2]]
    for i in range(3, n+1):
        n_list_1.append(n_list_2[i-1] + score_list[i])
        n_list_2.append(max(n_list_1[i-2], n_list_2[i-2]) + score_list[i])
    print(max(n_list_1[n], n_list_2[n]))
else:
    print(score_list[1])