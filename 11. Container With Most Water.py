# Partial solution
arr = [1,8,6,2,5,4,8,3,7]
# arr = [1,1]
n = len(arr)
max_val = 0
for i in range(n):
    for j in range(i, n):
        cur_max = abs(j-i * min(arr[i], arr[j]))
        print(i-j, arr[i], arr[j], j-i * min(arr[i], arr[j]))
        max_val = max(cur_max, max_val)
print(max_val)

