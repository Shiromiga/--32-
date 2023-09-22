import math
x = 0.4*10**4
y = -0.875
z = -0.475*10**-3
a = abs(math.cos(x)- math.cos(y))
b = (1+2*(math.sin(y)*math.sin(y)))
c = (1+z+((z**2)/2)+((z**3)/3)+((z**4)/4))
s = a**b*c
print("s = {0:.4f}".format(s))
                                    
