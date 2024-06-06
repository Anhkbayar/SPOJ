inputNum = input()
num_list = inputNum.split()
res = [int(i) for i in num_list]

a = res[0]
n = res[1]

if n<10:
    for i in range(1, n+1):
        p = pow(a, i)
        print(str(a)+"^"+str(i)+"="+str(p))
else:
    print("NO")