
def search(arr, el):
    try:
        if not len(arr):
            return None
        mid = (len(arr)-1)//2
        guess = arr[mid]
        if el == guess:
            return mid
        if el < guess:
            return 0 + search(arr[:mid], el) 
        else:
            return mid + 1 + search(arr[mid+1:], el)
    except:
        return "Not Found"

arr = [1,2,3,4,5,6,7,8,9,10]
print(search(arr, 6))