import numpy as np
import time
import copy

def bubble_sort_iteration(a, reverse=False):
    print "bubble_sort_iteration()"
    
    n = len(a)
    
    if not reverse:
        # sort ascending
        for i in range(n-1):
            if a[i] > a[i+1]:   
#                swap in python
                a[i], a[i+1] = a[i+1], a[i]
        
    else:
        # sort descending
        for i in range(n-1):
            if a[i] < a[i+1]:   
#                swap in python
                a[i], a[i+1] = a[i+1], a[i]
        
    




def init_data_matrix(data_matrix):
    print "init_data_matrix()"
    
    n = data_matrix.shape[1]
    
    
    #Create random 1d array
    randRow = np.random.randint(0, 10, n)
    print randRow
    
    
    data_matrix[n] = randRow
#    print data_matrix
    
    tmpRow = copy.deepcopy(randRow)
    
    # fill data matrix with columns 
    # (sorted ascending, ... random row ... , sorted descending)
    for k in reversed( range(0, n) ) :
#       bubble_sort_iteration
        bubble_sort_iteration(tmpRow)
#        insert partly sorted randRow
        data_matrix[k] = tmpRow
        
    
#    print data_matrix
    
    
    tmpRow = copy.deepcopy(randRow)
    
    for k in range(n+1, 2*n+1):
#       bubble_sort_iteration reverse
        reverse = True
        bubble_sort_iteration(tmpRow, reverse)
#        insert partly sorted randRow
        data_matrix[k] = tmpRow
        
    
#    print data_matrix




def qsort_simple(a):
    print "qsort_simple(a)"
    
#    numbers of comparison and moving operations for KEYS only
#    (not values)
    cmpCount = 0
    mvCount = 0
    
    
    return cmpCount, mvCount



def qsort_choice(a):
    print "qsort_choice(a)"
    
#    numbers of comparison and moving operations for KEYS only
#    (not values)
    cmpCount = 0
    mvCount = 0
    
    
    return cmpCount, mvCount





