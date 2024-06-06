import math
inputNum = input()
num_list = inputNum.split()
res = [float(i) for i in num_list]
a = res[0]
b = res[1]
c = pow(a, 2) + pow(b, 2)
nigger = math.sqrt(c)
formatted = "{:.1f}".format(nigger)
print(formatted)