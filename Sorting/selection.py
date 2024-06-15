def selection_sort(arr):
    new_list = []
    
    
    while arr:
        minimum = float('inf')
        minimum_position = 0
        for i, el in enumerate(arr):
            if el < minimum:
                minimum = el
                minimum_position = i
        
        del arr[minimum_position]
        new_list.append(minimum)

    return new_list
        
