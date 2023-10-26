
#Q1: program to input two real vectors
n = int(input("Enter the Dimensions of Vectors: "))
u = list()
print("Enter the vector u: ")
for i in range(0,n):
    p = int(input())
    u.append(p)
    print("Vectors u is: ",u)

v = list()
print("Enter the vector v: ")
for i in range(0,n):
    p = int(input())
    v.append(p)
    print("Vectors v is: ",v)

#q2: linear combination of two vectors
def combine(a,b):
    c = [0]*n;
    for i in range(0,n):
        c[i] = a * u[i]+ b*v[i]
    return c

#q3: find product of two vectors
def product():
    s = 0
    for i in range(0,n):
        s = s + u[i]*v[i]
    return s
