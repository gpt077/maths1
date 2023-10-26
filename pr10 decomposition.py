#program to find all divisors of given integers
def Divisors(n):
    u = [0]*n
    count = 0
    for i in range(1,n+1):
        if n%i == 0:
            u[count]=i
            count += 1
    d = [0]*count
    for i in range(0,count):
        d[i] = u[i]
    return d

#program to find the sum of all the divisors of given integers
def Div_sum(n):
    return sum(Divisors(n))

#program to find between 1 to 10000
def sum_check(n):
    if Div_sum(n)-n ==n:
        print("Sum of divisors of ",n,"is",Div_sum(n)-n)

def Numbers(x):
    for i in range(3,x):
        sum_check(i)
