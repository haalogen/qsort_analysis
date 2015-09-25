import sys
import numpy as np
import func as fu

    


# Create data_matrix N = 10
N = 4

data_matrix = np.zeros( (2 * N + 1, N) )

fu.init_data_matrix(data_matrix)

print data_matrix

rowsNum = data_matrix.shape[0] # == 2N+1

cmpSimple = np.zeros(rowsNum)
mvSimple = np.zeros(rowsNum)
cmpChoice = np.zeros(rowsNum)
mvChoice = np.zeros(rowsNum)


for k in range(rowsNum):
     cmpSimple[k], mvSimple[k] = fu.qsort_simple(data_matrix[k])
     cmpChoice[k], mvChoice[k] = fu.qsort_choice(data_matrix[k])
     




#while n < 1e10:
    # Create random vector[n]
    
    # qsort_simple(data_matrix[i,:]) counting Comparisons and Movings
    # qsort_choice((data_matrix[i,:])) counting Comparisons and Movings
#    save  C1 ,M1; C2, M2 numbers for each column
