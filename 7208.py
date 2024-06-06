num = input()
num_list = num.split()
res = [int(i) for i in num_list]

a = res[0]
n = res[1]

p = pow(a,n)
print(p)


