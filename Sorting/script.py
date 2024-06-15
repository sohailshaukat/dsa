from bubble import bubble_sort
from selection import selection_sort
from qsort import q_sort

import sys
sys.setrecursionlimit(15000)

# import random
import time

# x = 10**6
# unsorted_f = open('unsorted.txt', 'w')
# sorted_f = open('sorted.txt','w')

# list_of_numbers = [random.randrange(x) for _ in range(x)]

# unsorted_f.write(str(list_of_numbers))
# unsorted_f.close()

# sorted_f.write(str(sorted(list_of_numbers)))
# sorted_f.close()


unsorted_f = open('unsorted.txt', 'r')
unsorted_l = eval(unsorted_f.read())
unsorted_f.close()

sorted_f = open('sorted.txt', 'r')
sorted_l = eval(sorted_f.read())
sorted_f.close()


def time_function(foo):
    start_time = time.time()
    result = foo()
    end_time = time.time()
    return result, (end_time - start_time) * 1000

new_sorted, duration = time_function(lambda : sorted(unsorted_l))

print('Built In Sort', duration, new_sorted == sorted_l)

bubble_sorted, duration = time_function(lambda: bubble_sort(unsorted_l))

print('Bubble Sort', duration, bubble_sorted == sorted_l)

quick_sorted, duration = time_function(lambda : q_sort(unsorted_l[:]))

print('Quick Sort', duration, quick_sorted == sorted_l)

selection_sorted, duration = time_function(lambda : selection_sort(unsorted_l[:]))

print('Selection Sort', duration, selection_sorted == sorted_l)
