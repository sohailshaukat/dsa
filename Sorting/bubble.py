def bubble_sort(arr):
   
    length = len(arr) 

    run = 0

    while run < length-1:
       
        ptr = 0
        while ptr < length-1:
            if arr[ptr] > arr[ptr+1]:
                arr[ptr+1], arr[ptr] = arr[ptr], arr[ptr+1]
            ptr += 1
        run+=1
       
    return arr
       
