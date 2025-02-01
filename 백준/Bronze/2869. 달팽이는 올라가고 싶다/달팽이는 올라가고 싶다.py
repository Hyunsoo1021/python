a, b, c = map(int, input().split())
up = a - b
left = c - a
time = 1
left /= up
if left % 1 != 0:
    left -= (left % 1)
    left += 1
time += int(left)
print(time)
