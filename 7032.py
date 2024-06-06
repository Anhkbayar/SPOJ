import math 
lenth = float(input())
pi = 3.141592
r = lenth/2/pi
area = pi*pow(r, 2)
formatted = "{:.4f}".format(area) 
print(formatted)
