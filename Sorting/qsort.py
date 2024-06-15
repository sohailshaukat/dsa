import random

def q_sort(arr):
    if len(arr) < 2:
        return arr
    
    else:    
        k = random.randrange(len(arr)-1)
        pivot = arr[k]
        
        del arr[k]
        
        less = [ i for i in arr if i <= pivot ]
        
        greater = [ i for i in arr if i > pivot]
        
        
        return q_sort(less) + [pivot] + q_sort(greater) 
