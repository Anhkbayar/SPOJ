inputNum = input()
num_list = inputNum.split()
res = [int(i) for i in num_list]

current_max = res[0] 

for i in range(1, len(res)):
    if res[i] < current_max:
        res[i] = current_max
    else:
        current_max = res[i] 
