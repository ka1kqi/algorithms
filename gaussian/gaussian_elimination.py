import numpy as np
import math

"""
#param A, an m x n augmented matrix 
"""
def _gaussian_elimination_(A):
    rows = len(A)
    cols = A[0].size
    if rows == 1 or cols ==1:
        print("Invalid matrix")
        return
    row = 0

    #col represents the index of our current pivot
    for col in range(cols-1):
        print("Current matrix state ")
        print("Row " + str(row) + " Col: "+ str(col))
        print_matrix(A)
        #max_index = np.argmax(A[row:, col])
        max_index = get_col_max(A,row,col)
        if(A[max_index,col]==0):
            print("Free variable in this column, infinite solutions")
            continue
        swap(A,row,max_index)
        print("Swap row "+ str(row) + " with row " + str(max_index))
        print_matrix(A)

        for i in range(row+1,rows):
            f_ = A[i,col] / A[row,col]
            for j in range(col+1,cols):
                A[i,j] -= A[row,j]*f_
            A[i,col]=0
            print("Update row " + str(i))
            print_matrix(A)
        row+=1

"""
@param A an augmented m x n matrix
currently buggy, needs fix
"""
def _gauss_jordan_(A):
    print("reducing gauss jordan")
    rows = len(A)
    cols = A[0].size

    row = rows-1
    #start from cols-2 since the last column is not a pivot
    col = cols-2
    while col > -1:
        pivot_value = A[row,col]
        #we can't divide by 0
        if pivot_value==0:
            if A[row,cols-1]!=0:
                print("System has no solution")
                exit(0)
            row-=1
            continue
        #reduce each element in row
        for i in range(col,cols):
            A[row,i]/=pivot_value
        for i in range(row):
            for j in range(cols-1,col-1,-1):
                A[i,j]-=A[i,col]*A[row,j]
        print_matrix(A)
        row-=1
        col-=1

"""
@param A an augmented m x n matrix
"""
def rref(A):
    _gaussian_elimination_(A)
    _gauss_jordan_(A)
    print("Row reduced echelon form: ")
    print_matrix(A)

#max in column after row
def get_col_max(A,r,c):
    if r == len(A)-1:
        return r
    mx=r
    row = r+1
    for i in range(len(A)):
        if A[row,c] > A[mx,c]:
            mx=row
    return mx

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
            #print("%.2f"%A[r,c],end='\t')
            print(str(A[r,c]),end='\t')
        print()
    print()