num = int(input())
seq = 0
ans = 0
pro = list(map(int, input().split()))
for i in range(num):
    if pro[i] == 1:
        ans += 1
        if i != 0:
            if pro[i - 1] == 1:
                seq += 1
                ans += seq
            else:
                seq = 0
        else:
            pass
    else:
        pass
print(ans)
