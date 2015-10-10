import sys
import numpy as np
import func as fu
import copy
import time


def main():
    N = 6
    M = 6
    TIMES = 10
    ROWS_NUM = 2 * N + 1

    if len(sys.argv) >= 4:
        N = int(sys.argv[1])
        M = int(sys.argv[2])
        TIMES = int(sys.argv[3])
        ROWS_NUM = 2 * N + 1
    else:
        print """
Usage: 
    python analysis.py [len_array] [len_selectsort] [num_experiments]
Ex:
    python analysis.py 5 5 1
"""
        sys.exit(-1)
    
    time_qsort = 0
    time_qselect = 0
    
    
    cmp_simple = np.zeros(ROWS_NUM)
    swp_simple = np.zeros(ROWS_NUM)
    cmp_select = np.zeros(ROWS_NUM)
    swp_select = np.zeros(ROWS_NUM)
        
    
    for tm in range(TIMES):
        print "Iteration # %r." % tm
        data_matrix = np.zeros( (ROWS_NUM, N) )
        
        fu.init_data_matrix(data_matrix)
        
    #    print "Initial stand:"
    #    print data_matrix[   :N], '\n'
    #    print data_matrix[N:N+1], '\n'
    #    print data_matrix[N+1: ], '\n'
        
        
        data_matrix2 = copy.deepcopy(data_matrix)
        sorted_array = data_matrix[0]
        
        
        start_qsort = time.time()
        for k in range(ROWS_NUM):
            fu.qsort(data_matrix[k])
            cmp_simple[k] += fu.glob_cmp_cnt
            swp_simple[k] += fu.glob_swp_cnt
        
        finish_qsort = time.time()
        time_qsort += finish_qsort - start_qsort
        
        
        qsort_is_correct = [False] * ROWS_NUM
        for k in range(ROWS_NUM):
            if all(data_matrix[k] == sorted_array):
                qsort_is_correct[k] = True
        
        
        print "qsort_is_correct: ", all(qsort_is_correct)
            
        
        start_qselect = time.time()
        for k in range(ROWS_NUM):
            fu.qsort_select(data_matrix2[k], M)
            cmp_select[k] += fu.glob_cmp_cnt
            swp_select[k] += fu.glob_swp_cnt
        
        finish_qselect = time.time()
        time_qselect += finish_qselect - start_qselect
        
        
        qsort_select_is_correct = [False] * ROWS_NUM
        for k in range(ROWS_NUM):
            if all(data_matrix2[k] == sorted_array):
                qsort_select_is_correct[k] = True
        
        
        print "qsort_select_is_correct: ", all(qsort_select_is_correct)
        
#        print "cmp_simple:", cmp_simple
#        print "swp_simple:", swp_simple
#        print "cmp_select:", cmp_select
#        print "swp_select:", swp_select
#        print "\n"
    
    cmp_simple /= TIMES
    swp_simple /= TIMES
    cmp_select /= TIMES
    swp_select /= TIMES
    time_qsort /= TIMES
    time_qselect /= TIMES
    print "\nStatistics (mean values):"
    print "cmp_simple:", cmp_simple
    print "swp_simple:", swp_simple
    print "cmp_select:", cmp_select
    print "swp_select:", swp_select
    
    print "time_qsort: %r sec" % time_qsort
    print "time_qselect: %r sec \n" % time_qselect

    
    
#    print "Sorted (ascending) by qsort() stand 'data_matrix':"
#    print data_matrix[   :N], '\n'
#    print data_matrix[N:N+1], '\n'
#    print data_matrix[N+1: ], '\n'
    
#    print "Sorted (ascending) by qsort_select() stand 'data_matrix2':"
#    print data_matrix2[   :N], '\n'
#    print data_matrix2[N:N+1], '\n'
#    print data_matrix2[N+1: ], '\n'
    


if __name__ == '__main__':
    main()
