inputNum = input()
num_list = inputNum.split()
res = [int(i) for i in num_list]

b = res[0]
c = res[1]
d = res[2]

a = b*c-d
print(a)