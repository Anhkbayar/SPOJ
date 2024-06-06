inputNum = input()
num_list = inputNum.split()
res = [int(i) for i in num_list]

a = res[0]
b = res[1]
c = res[2]

if a+b>c and a+c>b and b+c>a :
    print("YES")
else:
    print("NO")