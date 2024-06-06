inputNum = input()
num_list = inputNum.split()
res = [eval(i) for i in num_list]  

if res[0] < res[1]:
    print(res[0])
else:
    print(res[1])
