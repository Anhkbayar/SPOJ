inputNum = input()
num_list = inputNum.split()
res = [int(i) for i in num_list]
mult = 1

for i in range(0, len(res)):
    if res[i]<5:
        mult*=res[i]
print(mult)