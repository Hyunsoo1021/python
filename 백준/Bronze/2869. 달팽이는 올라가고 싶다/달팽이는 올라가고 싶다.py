a, b, v = map(int, input().split())
num = (v-a)/(a-b)
if num%1 != 0:
    print(int(num)+2)
else:
    print(int(num)+1)
