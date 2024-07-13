
def search(arr, el):
    try:
        if not len(arr):
            return None
        mid = (len(arr)-1)//2
        guess = arr[mid]
        if el == guess:
            return mid
        if el < guess:
            return search(arr[:mid], el) 
        else:
            return mid + 1 + search(arr[mid+1:], el)
    except :
        return None

arr = list(range(1,11))
for i in range(0,11):
    print(search(arr, i))
