import numpy as np

"""""""""""""""""""""""""""""""""""
@param matrix A
@output 
"""""""""""""""""""""""""""""""""""
def _gaussian_elimination_(A):
    rows = len(A)
    cols = len(A[0])
    row = 0

    for col in range(cols):
        max_index = np.argmax(A[row:, col])
        swap(A,row,max_index)

        if(A[row,col]==0):
            continue

        for i in range(row+1,rows):
            f_ = A[i,col] / A[row,col]
            for j in range(col+1,cols):
                A[i,j] -= A[row,j]*f_
            A[i,col]=0

        row+=1

    print_matrix(A)

#swap row x with row y
def swap(A,x,y):
    if x==y:
        return
    temp = A[y]
    temp = np.array(temp)
    A[y]=A[x]
    A[x]=temp

def print_matrix(A):
    for r in range(len(A)):
        for c in range(len(A[r])):
            print(str(A[r,c]),end='\t')
        print()

A = np.array(
    [ 
      [1,2,3,4],
      [4,5,6,5],
      [7,8,9,10],
      [4,7,1,3]
    ])

print_matrix(A)
#_gaussian_elimination_(A)
