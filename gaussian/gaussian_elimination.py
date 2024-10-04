import numpy as np

""""""""""""""""""""""""""""""""""
@param matrix A
@output 
""""""""""""""""""""""""""""""""""
def gaussian_elimination_(A):
    rows = len(A)
    cols = len(A[0])

    for i in range(cols):
        
