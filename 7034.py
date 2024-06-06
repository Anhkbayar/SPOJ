import math
numbers = input().strip()
x1,x2 = map(float, numbers.split())

arith = (x1+x2)/2
geo = math.sqrt(x1*x2)

print(f"{arith:.2f} {geo:.2f}")