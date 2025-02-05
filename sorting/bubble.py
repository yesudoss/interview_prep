l = [2,1,3,4,5]
n = len(l) - 1
for i in range(n):
    swapped = False
    for j in range(0, n-i):
        if l[j] > l[j+1]:
            l[j], l[j+1] = l[j+1], l[j]
            print(l)
            swapped=True
    if not swapped:
        break
print(l)
    
