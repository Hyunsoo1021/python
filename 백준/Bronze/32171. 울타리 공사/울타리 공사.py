n = int(input())
lx1, ly1, lx2, ly2 = 0, 0, 0, 0
for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    if i == 0:
        lx1, ly1, lx2, ly2 = x1, y1, x2, y2
    else:
        lx1 = min(lx1, x1)
        ly1 = min(ly1, y1)
        lx2 = max(lx2, x2)
        ly2 = max(ly2, y2)
    print(2 * ((lx2-lx1)+(ly2-ly1)))
