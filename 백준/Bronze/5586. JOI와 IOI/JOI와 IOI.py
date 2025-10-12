a = input()
joi = 0
ioi = 0
for i in range(len(a)-2):
    if a[i] == 'J' and a[i+1] == 'O' and a[i+2] == 'I':
        joi+=1
    elif a[i] == 'I' and a[i+1] == 'O' and a[i+2] == 'I':
        ioi+=1
print(joi)
print(ioi)