import sys
import numpy as np
import func as fu
import copy

def main():
    # Create data_matrix N = 10
    N = 10
    m = 6

    data_matrix = np.zeros( (2 * N + 1, N) )

    fu.init_data_matrix(data_matrix)

    #print data_matrix[   :N], '\n'
    print data_matrix[N:N+1], '\n'
    #print data_matrix[N+1: ], '\n'

    rowsNum = data_matrix.shape[0] # == 2N+1

    cmpSimple = np.zeros(rowsNum, dtype=int)
    mvSimple = np.zeros(rowsNum, dtype=int)
    cmpSelect = np.zeros(rowsNum, dtype=int)
    mvSelect = np.zeros(rowsNum, dtype=int)

    data_matrix2 = copy.deepcopy(data_matrix)

    #for k in range(rowsNum):
    #     fu.qsort_simple(data_matrix[k], 0, N-1, cmpSimple[k], mvSimple[k])
    #     fu.qsort_choice(data_matrix2[k], 0, N-1, cmpSelect[k], 
    #                        mvSelect[k], 4)

    fu.qsort(data_matrix[N], cmpSimple[N], mvSimple[N])

    fu.qsort_select(data_matrix2[N], m, cmpSelect[N], mvSelect[N])

    #print cmpSimple
    #print mvSimple
    #print cmpSelect
    #print mvSelect


    #print data_matrix[   :N], '\n'
    print data_matrix[N:N+1], '\n'
    #print data_matrix[N+1: ], '\n'


if __name__ == '__main__':
    main()
