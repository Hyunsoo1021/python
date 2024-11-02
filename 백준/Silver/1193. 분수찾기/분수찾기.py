x = int(input())
parent = 0
plus_num = 0
start_num = 1
total = 0
while True:
    start_num += plus_num
    if start_num > x:
        start_num -= plus_num
        total = plus_num + 1
        break
    plus_num += 1
if plus_num % 2 == 0:
    parent = total - (x-start_num) - 1
else:
    parent = x-start_num + 1
print(f'{total-parent}/{parent}')
