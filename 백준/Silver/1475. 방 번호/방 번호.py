n = input()
num_array = list()
for _ in range(10):
    num_array.append(0)
for i in range(len(n)):
    num = int(n[i])
    if num == 6 or num == 9:
        if num_array[6] >= num_array[9]:
            num_array[9] += 1
        else:
            num_array[6] += 1
    else:
        num_array[num] += 1
print(max(num_array))