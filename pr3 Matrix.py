#input two matices
m = int(input("Enter the no. of Rows in Matrics A and B: "))
n = int(input("Enter the no. of Columns in Matrics A and B: "))

A = []
for i in range(0,m):
    A.append([])
    A[i] = [0]*n
    for j in range(0,n):
        print("Entry of matrix A[",i+1,",",j+1,"]=")
        A[i][j] = int(input())
print("Matrix A: ")
for i in range(0,m):
    print(A[i])
B=[]
for i in range(0,m):
    B.append([])
    B[i] = [0]*n
    for j in range(0,n):
        print("Entry of matrix B[",i+1,",",j+1,"]=")
        B[i][j] = int(input())
print("Matrix B: ")
for i in range(0,m):
    print(B[i])

#add two matices
def AddMat(A,B):
    C = []
    for i in range(0,m):
        C.append([])
        C[i] = [0]*n
        for j in range(0,n):
            C[i][j] = A[i][j] + B[i][j]
    print("Matrix A+B: ")
    for i in range(0,m):
            print(C[i])

#find scalar multiplication of matrix
def ScaleMul(A,k):
    C = []
    for i in range(0,m):
        C.append([])
        C[i] = [0]*n
        for j in range(0,n):
            C[i][j] = A[i][j]*k
    print("Matrix kA: ")
    for i in range(0,m):
        print(C[i])

#find transpose of matrix
def TransMat(A):
    C = []
    for i in range(0,n):
        C.append([])
        C[i] = [0]*m
        for j in range(0,m):
            C[i][j] = A[j][i]
    return C

#display specific row and column

def DisRow(A,r):
    return A[r-1]

def DisCol(A,c):
    for i in range(0,m):
        print([A[i][c-1]])

def PrintCol(A,c):
    return DisRow(TransMat(A),c)
