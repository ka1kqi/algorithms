import gaussian_elimination as gauss
import numpy as np


A = np.array(
    [ 
        [1,3,1,4],
        [3,2,3,5],
        [4,0,3,7]
    ]
)
A=A.astype(float)
#gauss.rref(A)

A=np.array(
    [
        [1,6,2,-5,-2,-4],
        [0,0,2,-8,-1,3],
        [0,0,0,0,1,7]
    ]
)
#A=A.astype(float)
gauss.rref(A)





