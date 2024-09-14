q = int(input())
prob = 0
you_die = False
for i in range(q):
    a, b = map(int, input().split())
    if a == 1:
        prob+=b
    elif a == 2:
        prob-=b
        if prob < 0:
            you_die = True
            break
if you_die is True:
    print('Adios')
elif you_die is False:
    print('See you next month')