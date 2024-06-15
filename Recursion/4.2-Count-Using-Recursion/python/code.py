def length(arr):
    if(not arr): return 0
    return 1 + length(arr[1:])

arr = [1, 2, 3, 4]
print(length(arr))
