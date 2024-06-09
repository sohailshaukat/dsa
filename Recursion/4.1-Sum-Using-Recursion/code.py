#! python3

def sum(arr):
    if not len(arr):
        return 0;
    return arr.pop() + sum(arr)


arr = [1, 2, 3, 4]
print(sum(arr))
