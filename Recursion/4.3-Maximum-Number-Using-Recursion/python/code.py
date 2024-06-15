
def maximum(arr):
    if len(arr) == 1:
        return arr.pop();
    current = arr[1]
    other = maximum(arr[1:])
    return current if current > other else other


arr = [1,2,4,3]

print(maximum(arr))