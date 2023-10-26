#program to input matrix and display determinant and inverse of that matrix

import numpy as np
n = int(input("Enter the number of rows in matrix A: "))
M = []
for i in range(0,n):
    M.append([])
    M[i] = [0]*n
    for j in range(0,n):
        print("Entry of matrix A[",i+1,",",j+1,"]=")
        M[i][j] = int(input())
print("The matrix M is: \n",np.mat(M))
a = np.linalg.det(M)
print("Deteminant of Matrix M is: ",a)
if a!=0:
    Minv = np.linalg.inv(M)
    print("The inverse of the matrix M is: ",np.mat(Minv))
else:
    print("Matrix is not Invertible")

#program to find eigen value and eigen vectors of Matrix A

A = np.mat("1,-1,0;2,-1,0;0,-1,1")

def eigen(A):
    import numpy as np
    print("A:\n",A)
    e_values,e_vectors = np.linalg.eig(A)
    print("\n eigen values are: \n",e_values)
    print("\n eigen vectors are: \n",e_vectors)
