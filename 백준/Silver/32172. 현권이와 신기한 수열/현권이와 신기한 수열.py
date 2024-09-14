num = int(input())
num_dic = {0: True}
a = 0
for i in range(num):
    if a - (i+1) >=0 and (a - (i+1)) not in num_dic:
        a = a - (i+1)
    else:
        a = a + (i+1)
    num_dic[a] = True
print(a)