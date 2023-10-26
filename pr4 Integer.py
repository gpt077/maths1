#Q1 find a and b such that N = a^2-b^2 for N>5

def Numbers(N):
    a = 1
    for i in range(2,int(N/2)):
        if N%2 == 0:
            a = i
            b = N/i
            x,y = (a+b)*0.5,(a-b)*0.5
            break
        else:
            x = (N-1)/2
            y = x+1
        if abs(x) < abs(y):
            x,y = y,x
    print("Value of a: ",abs(x))
    print("Value of b: ",abs(y))
    d = x*x - y*y
    print("Value of N: ",abs(d))

#Q2: find GCD of two integers

def GCD(a,b):
    x = abs(a)
    y = abs(b)
    r = 1
    if x < y:
        x,y = y,x
    if y == 0:
        if x == 0:
            print("GCD of ",a," and ",b," is not defined")
        else:
            print("GCD of ",a," and ",b," is: ",x)
    else:
        while r!=0:
            r = x%y
            x = y
            y = r
        return x

#q3 find LCM of two integers
def LCM(a,b):
    print("LCM of ",a," and ",b," is: ",abs(a*b)/GCD(a,b))
