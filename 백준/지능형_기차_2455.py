a = 0
b = 0
for i in range(4):
    out, ins = input().split()
    out = int(out)
    ins = int(ins)
    b -= out
    b += ins
    if a < b:
        a = b
print(a)
