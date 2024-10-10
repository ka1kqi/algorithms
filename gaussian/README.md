# Gaussian Elimination

Row reduction algorithm for matrices

The algorithm works by finding the largest number in the current column, which becomes our pivot. We then reduce the other columns by subtracting the row from every other row so that the other values in the column are 0, meaning there should only be 1 value that isn't 0 in every column. 
Row echelon form also says that the value that is not 0 must be above all the values that are 0.

Afterwards we perform a Gauss Jordan elimination to reduce the matrix into Row Reduced Echelon Form. We start from the bottom row and work up by reducing the elements above it to 0 as well as the augmented column so we are in RREF. We do this for every row until we reach our final RREF.  

Run the gaussian_examples.py file to see output
You can modify the matrices used within the file as well, but beware that currently the program only works on augmented matrices,
i.e. the last column will not be used as a pivot.
