s = 0
e = 0
while True:
    s,e = map(int, input().split())
    if s % 1 == 0 and e % 1 == 0 and 2<=s<=9 and 2<=e<=9:
        break
    else:
        print("INPUT ERROR!")
        continue
for i in range(1, 10):
    pr_str = ""
    if s<=e:
        for j in range(s, e+1):
            pr_str += f"{j} * {i} = {j*i:2}"
            if j != e:
                pr_str+='   '
    elif s>e:
        for j in range(s, e-1, -1):
            pr_str += f"{j} * {i} = {j * i:2}"
            if j != e:
                pr_str+='   '
    print(pr_str)
