def binary_search(arr: list, target: int) -> int:
    low = 0
    high = len(arr) - 1
    while high>=low:
        mid = low + (high-low) // 2 
        if target == arr[mid]:
            return mid
        elif target > arr[mid]:
            low = mid+1
        else:
            high = mid-1
    return -1
    
arr = [1,2,3,4,5,6,7]
target = 77
result = binary_search(arr, target)
print(result)
