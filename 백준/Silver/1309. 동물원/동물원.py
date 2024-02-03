n = int(input())
n_none = 1
n_left = 1
n_right = 1
n_new_none = 0
n_new_left = 0
n_new_right = 0
for i in range(2, n+1):
    n_new_none = n_none + n_left + n_right
    n_new_left = n_none + n_right
    n_new_right = n_none + n_left
    n_none = n_new_none
    n_left = n_new_left
    n_right = n_new_right
print((n_none + n_left + n_right)%9901)