rgb_len = int(input())
rgb = list(input())

for i in range(rgb_len):
    if rgb[i] == 'R':
        rgb[i] = 0
    elif rgb[i] == 'G':
        rgb[i] = 1
    else:
        rgb[i] = 2
rgb_origin = [] + rgb

count = 0
count_list = []
for i in range(3):
    rgb = [] + rgb_origin
    count = 0
    for j in range(rgb_len - 2):
        if rgb[j] != i:
            while True:
                rgb[j] = (rgb[j] + 1) % 3
                rgb[j + 1] = (rgb[j + 1] + 1) % 3
                rgb[j + 2] = (rgb[j + 2] + 1) % 3
                count += 1
                if rgb[j] != i:
                    continue
                else:
                    break
    if rgb[-1] == rgb[-2] == rgb[-3]:
        count_list.append(count)
if len(count_list) == 0:
    print(-1)
else:
    print(min(count_list))