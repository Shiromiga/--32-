import math
x = 12.3*10**-1
y = 15.4
z = 0.252*10**3
a = (y**(x+1))/((abs(y-2))**(1/3)+3)
b = ((x+(y/2))/(2*(abs(x+y))))
c = (x+1)**(-1/math.sin(z))
s = a+b*c
print("s = {0:.4f}".format(s))
                                    
