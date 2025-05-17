a = int(input())
count = 0
for i in range(1, a//3+1):
    maximum = (a - i) // 2
    if (a-2*i)/2 >= i:
        minimum = (a-2*i)//2+1
    else:
        minimum = i
    if minimum <= maximum:
        count += (maximum - minimum + 1)
print(count)