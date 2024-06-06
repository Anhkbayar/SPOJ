import math
inputNum = input()
num_list = inputNum.split()
res = [float(i) for i in num_list]
a = res[0]
b = res[1]
c = res[2]
s = (a+b+c)/2
area = math.sqrt(s*(s-a)*(s-b)*(s-c))
formatted = "{:.2f}".format(area) 
print(formatted)