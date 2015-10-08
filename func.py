import numpy as np
import time
import copy

def bubble_sort_iteration(a, reverse=False):
#    print "bubble_sort_iteration()"
    
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



def qsort(array, cmpCount, mvCount):
    _qsort(array, 0, len(array) - 1)


def _qsort(array, start, stop):
#    [start, stop]
    if stop - start > 0:
        randPos = np.random.randint(start, stop+1)
        pivot, left, right = array[randPos], start, stop
        
        while left <= right:
            while array[left] < pivot:
                left += 1
            while array[right] > pivot:
                right -= 1
            
            if left <= right:
                array[left], array[right] = array[right], array[left]
                left += 1
                right -= 1
                
        _qsort(array, start, right)
        _qsort(array, left, stop)
        

def _selectsort(array):
    N = len(array)
    
    
    for k in range(N):
        minInd = k
        for i in range(k+1, N):
            if array[i] < array[minInd]:
                minInd = i
#                print "min: ", array[minInd] 
            
        array[k], array[minInd] = array[minInd], array[k]



def qsort_select(array, m, cmpCount, mvCount):
    _qsort_select(array, 0, len(array) - 1, m)


def _qsort_select(array, start, stop, m):
#    [start, stop]
    if stop - start + 1 <= m: # leq than m elements
        _selectsort(array[start : stop+1])
        
    else:
        randPos = np.random.randint(start, stop+1)
        pivot, left, right = array[randPos], start, stop
        
        while left <= right:
            while array[left] < pivot:
                left += 1
            while array[right] > pivot:
                right -= 1
            
            if left <= right:
                array[left], array[right] = array[right], array[left]
                left += 1
                right -= 1
                
        _qsort_select(array, start, right, m)
        _qsort_select(array, left, stop, m)






