def add(z1,z2):
    x1 = z1.real
    y1 = z1.imag
    x2 = z2.real
    y2 = z2.imag
    x = x1+y1
    y = x2+y2
    return complex(x,y)


a="hello world"

lilioalaosos


lolololololololololollolo
def multiply(z1,z2):
    x1 = z1.real
    y1 = z1.imag
    x2 = z2.real
    y2 = z2.imag
    x = x1*x2 - y1*y2
    y = x1*y2 + x2*y1
    return complex(x,y)

def conjugate(z):
    x = z.real
    y = z.imag
    return complex(x,-y)

def divide(z1,z2):
    z = multiply(z1,conjugate(z2))
    x = z2.real
    y = z2.imag
    z = z/(x**2+y**2)
    return z

def rotate(z,t):
    import cmath as m
    p = m.phase(z)
    r = abs(z)
    p = p+t*m.pi/180
    z = m.rect(r,p)
    return z

def scale_rotate(z,t,scale):
    import cmath as m
    p = m.phase(z)
    r = abs(z)
    p = p + t*m.pi/180
    z = m.rect(scale*r,p)
    return z
