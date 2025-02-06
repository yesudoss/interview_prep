# bubble sort
def bubble_sort(arr: list, n: int) -> list:
    for i in range(0, n-1):
        swapped=False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1], swapped = arr[j+1], arr[j], True
        if not swapped:
            break
    return arr


arr = [2,1,6,43,8,99,64,3]
n = len(arr)
result = bubble_sort(arr, n)
print(result)
