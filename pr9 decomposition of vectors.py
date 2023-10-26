Python 3.12.0 (tags/v3.12.0:0fb18b0, Oct  2 2023, 13:03:39) [MSC v.1935 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

===== RESTART: C:/Users/Vishant-PC/Desktop/LA PRACTICALS/complex numbers.py ====
add(3+5j,5+3j)
(8+8j)
multiply(3+5j,5+3j)
34j
multiply(3+5j,1+3j)
(-12+14j)
conjugate(3+5j)
(3-5j)
divide(3+5j,5+3j)
(0.8823529411764706+0.47058823529411764j)
rotate(3+5j,90)
(-5+3.0000000000000004j)
scale_rotate(3+5j,90,2)
(-10+6.000000000000001j)

= RESTART: C:/Users/Vishant-PC/Desktop/LA PRACTICALS/pr2 vectors.py
Enter the Dimensions of Vectors: 2
Enter the vector u: 
3
Vectors u is:  [3]
4
Vectors u is:  [3, 4]
Enter the vector v: 
Traceback (most recent call last):
  File "C:/Users/Vishant-PC/Desktop/LA PRACTICALS/pr2 vectors.py", line 14, in <module>
    p = int(input())
KeyboardInterrupt

= RESTART: C:/Users/Vishant-PC/Desktop/LA PRACTICALS/pr2 vectors.py
Enter the Dimensions of Vectors: 3
Enter the vector u: 
2
Vectors u is:  [2]
3
Vectors u is:  [2, 3]
4
Vectors u is:  [2, 3, 4]
Enter the vector v: 
5
Vectors v is:  [5]
6
Vectors v is:  [5, 6]
7
Vectors v is:  [5, 6, 7]
combine(2,3)
[19, 24, 29]
product()
56

= RESTART: C:/Users/Vishant-PC/Desktop/LA PRACTICALS/pr3 Matrix.py
Enter the no. of Rows in Matrics A and B: 3
Enter the no. of Columns in Matrics A and B: 2
Entry of matrix A[ 1 , 1 ]=
1
Entry of matrix A[ 1 , 2 ]=
2
Entry of matrix A[ 2 , 1 ]=
3
Entry of matrix A[ 2 , 2 ]=
4
Entry of matrix A[ 3 , 1 ]=
5
Entry of matrix A[ 3 , 2 ]=
6
Matrix A: 
[1, 2]
[3, 4]
[5, 6]
Entry of matrix B[ 1 , 1 ]=
1
Entry of matrix B[ 1 , 2 ]=
0
Entry of matrix B[ 2 , 1 ]=
2
Entry of matrix B[ 2 , 2 ]=
3
Entry of matrix B[ 3 , 1 ]=
4
Entry of matrix B[ 3 , 2 ]=
-1
Matrix B: 
[1, 0]
[2, 3]
[4, -1]
AddMat(A,B)
Matrix A+B: 
[2, 2]
[5, 7]
[9, 5]
ScaleMul(A,2)
Matrix kA: 
[2, 4]
[6, 8]
[10, 12]
TransMat(A)
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    TransMat(A)
  File "C:/Users/Vishant-PC/Desktop/LA PRACTICALS/pr3 Matrix.py", line 57, in TransMat
    C[i][j] = A[i][j]
IndexError: list index out of range
TransMat(A)
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    TransMat(A)
  File "C:/Users/Vishant-PC/Desktop/LA PRACTICALS/pr3 Matrix.py", line 57, in TransMat
    C[i][j] = A[i][j]
IndexError: list index out of range

= RESTART: C:/Users/Vishant-PC/Desktop/LA PRACTICALS/pr3 Matrix.py
Enter the no. of Rows in Matrics A and B: 3
Enter the no. of Columns in Matrics A and B: 2
Entry of matrix A[ 1 , 1 ]=
1
Entry of matrix A[ 1 , 2 ]=
2
Entry of matrix A[ 2 , 1 ]=
3
Entry of matrix A[ 2 , 2 ]=
4
Entry of matrix A[ 3 , 1 ]=
5
Entry of matrix A[ 3 , 2 ]=
6
Matrix A: 
[1, 2]
[3, 4]
[5, 6]
Entry of matrix B[ 1 , 1 ]=
1
Entry of matrix B[ 1 , 2 ]=
0
Entry of matrix B[ 2 , 1 ]=
2
Entry of matrix B[ 2 , 2 ]=
3
Entry of matrix B[ 3 , 1 ]=
4
Entry of matrix B[ 3 , 2 ]=
-1
Matrix B: 
[1, 0]
[2, 3]
[4, -1]
TransMat(A)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    TransMat(A)
  File "C:/Users/Vishant-PC/Desktop/LA PRACTICALS/pr3 Matrix.py", line 57, in TransMat
    C[i][j] = A[i][j]
IndexError: list index out of range

= RESTART: C:/Users/Vishant-PC/Desktop/LA PRACTICALS/pr3 Matrix.py
Enter the no. of Rows in Matrics A and B: 
= RESTART: C:/Users/Vishant-PC/Desktop/LA PRACTICALS/pr3 Matrix.py
Enter the no. of Rows in Matrics A and B: 3
Enter the no. of Columns in Matrics A and B: 2
Entry of matrix A[ 1 , 1 ]=
1
Entry of matrix A[ 1 , 2 ]=
2
Entry of matrix A[ 2 , 1 ]=
3
Entry of matrix A[ 2 , 2 ]=
4
Entry of matrix A[ 3 , 1 ]=
5
Entry of matrix A[ 3 , 2 ]=
6
Matrix A: 
[1, 2]
[3, 4]
[5, 6]
Entry of matrix B[ 1 , 1 ]=
1
Entry of matrix B[ 1 , 2 ]=
0
Entry of matrix B[ 2 , 1 ]=
2
Entry of matrix B[ 2 , 2 ]=
3
Entry of matrix B[ 3 , 1 ]=
4
Entry of matrix B[ 3 , 2 ]=
-1
Matrix B: 
[1, 0]
[2, 3]
[4, -1]
TransMat(A)
[[1, 3, 5], [2, 4, 6]]
disRow(A,2)
[3, 4]
DisCol(A,2)
[2]
[4]
[6]
PrintCol(A,2)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    PrintCol(A,2)
  File "C:/Users/Vishant-PC/Desktop/LA PRACTICALS/pr3 Matrix.py", line 70, in PrintCol
    return DisRow(TransMat(A),c)
NameError: name 'DisRow' is not defined. Did you mean: 'disRow'?

= RESTART: C:/Users/Vishant-PC/Desktop/LA PRACTICALS/pr3 Matrix.py
Enter the no. of Rows in Matrics A and B: 3
Enter the no. of Columns in Matrics A and B: 2
Entry of matrix A[ 1 , 1 ]=
1
Entry of matrix A[ 1 , 2 ]=
2
Entry of matrix A[ 2 , 1 ]=
3
Entry of matrix A[ 2 , 2 ]=
4
Entry of matrix A[ 3 , 1 ]=
5
Entry of matrix A[ 3 , 2 ]=
6
Matrix A: 
[1, 2]
[3, 4]
[5, 6]
Entry of matrix B[ 1 , 1 ]=
1
Entry of matrix B[ 1 , 2 ]=
0
Entry of matrix B[ 2 , 1 ]=
2
Entry of matrix B[ 2 , 2 ]=
3
Entry of matrix B[ 3 , 1 ]=
4
Entry of matrix B[ 3 , 2 ]=
-1
Matrix B: 
[1, 0]
[2, 3]
[4, -1]
PrintCol(A,2)
[2, 4, 6]

= RESTART: C:/Users/Vishant-PC/Desktop/LA PRACTICALS/pr4 Integer.py
Numbers(6)
Numbers(6)

= RESTART: C:/Users/Vishant-PC/Desktop/LA PRACTICALS/pr4 Integer.py
Numbers(6)
Value of a:  2.5
Value of b:  0.5
Value of N:  6.0
GCD(105,225)
15
GCD(0,0)
GCD of  0  and  0  is not defined
LCM(20,25)
LCM of  20  and  25  is:  100.0
GCD(20,25)
5

= RESTART: C:/Users/Vishant-PC/Desktop/LA PRACTICALS/pr5 Inverse matrix.py
Enter the number of rows in matrix A: 3
Entry of matrix A[ 1 , 1 ]=
1
Entry of matrix A[ 1 , 2 ]=
2
Entry of matrix A[ 1 , 3 ]=
3
Entry of matrix A[ 2 , 1 ]=
4
Entry of matrix A[ 2 , 2 ]=
5
Entry of matrix A[ 2 , 3 ]=
6
Entry of matrix A[ 3 , 1 ]=
7
Entry of matrix A[ 3 , 2 ]=
8
Entry of matrix A[ 3 , 3 ]=
9
The matrix M is: 
 [[1 2 3]
 [4 5 6]
 [7 8 9]]
Deteminant of Matrix M is:  0.0
Matrix is not Invertible
eigen(M)
A:
 [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

 eigen values are: 
 [ 1.61168440e+01 -1.11684397e+00 -1.30367773e-15]

 eigen vectors are: 
 [[-0.23197069 -0.78583024  0.40824829]
 [-0.52532209 -0.08675134 -0.81649658]
 [-0.8186735   0.61232756  0.40824829]]
eigen(A)
A:
 [[ 1 -1  0]
 [ 2 -1  0]
 [ 0 -1  1]]

 eigen values are: 
 [ 1.00000000e+00+0.j -9.71445147e-17+1.j -9.71445147e-17-1.j]

 eigen vectors are: 
 [[0.        +0.j         0.35355339+0.35355339j 0.35355339-0.35355339j]
 [0.        +0.j         0.70710678+0.j         0.70710678-0.j        ]
 [1.        +0.j         0.35355339+0.35355339j 0.35355339-0.35355339j]]

= RESTART: C:/Users/Vishant-PC/Desktop/LA PRACTICALS/pr8 Gram schmidth process.py
ips([1,2,1],[2,4,1])
11
norm([2,4,1])
4.58257569495584
unit([1,4,2])
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    unit([1,4,2])
  File "C:/Users/Vishant-PC/Desktop/LA PRACTICALS/pr8 Gram schmidth process.py", line 18, in unit
    p[i] = u[i]/num[u]
NameError: name 'num' is not defined. Did you mean: 'sum'?

= RESTART: C:/Users/Vishant-PC/Desktop/LA PRACTICALS/pr8 Gram schmidth process.py
unit([1,4,2])
Traceback (most recent call last):
  File "<pyshell#31>", line 1, in <module>
    unit([1,4,2])
  File "C:/Users/Vishant-PC/Desktop/LA PRACTICALS/pr8 Gram schmidth process.py", line 18, in unit
    p[i] = u[i]/nrm[u]
NameError: name 'nrm' is not defined. Did you mean: 'norm'?

= RESTART: C:/Users/Vishant-PC/Desktop/LA PRACTICALS/pr8 Gram schmidth process.py
unit([1,4,2])
Traceback (most recent call last):
  File "<pyshell#32>", line 1, in <module>
    unit([1,4,2])
  File "C:/Users/Vishant-PC/Desktop/LA PRACTICALS/pr8 Gram schmidth process.py", line 18, in unit
    p[i] = u[i]/sum[u]
TypeError: 'builtin_function_or_method' object is not subscriptable

= RESTART: C:/Users/Vishant-PC/Desktop/LA PRACTICALS/pr8 Gram schmidth process.py
unit([1,4,2])
[0.14285714285714285, 0.5714285714285714, 0.2857142857142857]

= RESTART: C:/Users/Vishant-PC/Desktop/LA PRACTICALS/pr8 Gram schmidth process.py
unit([1,4,2])
[0.2182178902359924, 0.8728715609439696, 0.4364357804719848]
proj([1,2,1],[1,4,2])
[0.5238095238095238, 2.0952380952380953, 1.0476190476190477]
sub([1,2,1],[1,4,2])
[1, 4, 2]
GSP([[1,1,1],[1,2,3],[4,5,6]])
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    GSP([[1,1,1],[1,2,3],[4,5,6]])
  File "C:/Users/Vishant-PC/Desktop/LA PRACTICALS/pr8 Gram schmidth process.py", line 45, in GSP
    un[i] = unit(u[i])
  File "C:/Users/Vishant-PC/Desktop/LA PRACTICALS/pr8 Gram schmidth process.py", line 16, in unit
    p = [0]*len(u)
TypeError: object of type 'int' has no len()

= RESTART: C:/Users/Vishant-PC/Desktop/LA PRACTICALS/pr8 Gram schmidth process.py
GSP([[1,1,1],[1,2,3],[4,5,6]])
Traceback (most recent call last):
  File "<pyshell#38>", line 1, in <module>
    GSP([[1,1,1],[1,2,3],[4,5,6]])
  File "C:/Users/Vishant-PC/Desktop/LA PRACTICALS/pr8 Gram schmidth process.py", line 45, in GSP
    un[i] = unit(u[i])
  File "C:/Users/Vishant-PC/Desktop/LA PRACTICALS/pr8 Gram schmidth process.py", line 16, in unit
    p = [0]*len(u)
TypeError: object of type 'int' has no len()
sub([1,2,1],[1,4,2])
[1, 4, 2]
>>> 
= RESTART: C:/Users/Vishant-PC/Desktop/LA PRACTICALS/pr8 Gram schmidth process.py
>>> GSP([[1,1,1],[2,3,4],[4,5,6]])
[[0.5773502691896258, 0.5773502691896258, 0.5773502691896258], [0.5773502691896257, 0.5773502691896257, 0.5773502691896257], [0.5773502691896257, 0.5773502691896257, 0.5773502691896257]]
>>> 
= RESTART: C:/Users/Vishant-PC/Desktop/LA PRACTICALS/pr8 Gram schmidth process.py
>>> GSP([[1,1,1],[2,3,4],[4,5,6]])
[[0.5773502691896258, 0.5773502691896258, 0.5773502691896258], [0.5773502691896257, 0.5773502691896257, 0.5773502691896257], [0.5773502691896257, 0.5773502691896257, 0.5773502691896257]]
>>> 
= RESTART: C:/Users/Vishant-PC/Desktop/LA PRACTICALS/pr9 decomposition of vectors.py
>>> ips([1,2,1],[1,4,2])
11
>>> ortho([1,2,3],[1,-1,1])
2
[1, 2, 3]  and  [1, -1, 1]  are not orthogonal
>>> proj([1,2,1],[2,4,1])
[1.0476190476190477, 2.0952380952380953, 0.5238095238095238]
>>> decompose([1,2,3],[2,4,1])
[1, 2, 3]  =  [1.2380952380952381, 2.4761904761904763, 0.6190476190476191]  +  [-0.23809523809523814, -0.4761904761904763, 2.380952380952381]
