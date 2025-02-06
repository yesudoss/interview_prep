# selection sort

def selection_sort(arr: list, n: int) -> list:
    for i in range(0,n-1):
        min_ind = i
        for j in range(i+1, n):
            if arr[j] < arr[min_ind]:
                min_ind = j
        arr[min_ind], arr[i] = arr[i], arr[min_ind]
    return arr

arr = [5,4,3,2]
n = len(arr)
result = selection_sort(arr, n)
print(result)
