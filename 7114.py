inputNum = input()
num_list = inputNum.split()
res = [int(i) for i in num_list]

for i in range(0,len(res)):
    if res[i]%2 == 0:
        print("YES")
    else:
        print("NO")