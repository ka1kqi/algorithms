import gaussian_elimination as gauss
import numpy as np

"""
This script reduced augmented matrices into Row Reduced Echelon Form
Idk why i made it so it only works on augmented matrices, perhaps
because thats what I was learning in class but idk
Will fix eventually to work on every matrix
"""

print("\033[91m-------------------------------------------------------\033[0m")
print("\033[91mExample 1\033[0m")
A = np.array(
    [ 
        [1,3,1,4],
        [3,2,3,5],
        [4,0,3,7]
    ]
)
A=A.astype(float)
gauss.rref(A)

print()
print("\033[91m-------------------------------------------------------\033[0m")
print()

print("\033[91mExample 2\033[0m")
B=np.array(
    [
        [3,0,0,0],
        [3,10,5,0],
        [4,20,7,0]
    ]
)
B=B.astype(float)
gauss.rref(B)





