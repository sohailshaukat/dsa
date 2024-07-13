
def search(arr, el):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        guess = arr[mid]
        if guess == el:
            return mid
        elif guess < el:
            low = mid + 1
        else:
            high = mid - 1

    return -1

arr = list(range(1,11))
for i in range(0,11):
    print(search(arr, i))