inputNum = input()
num_list = inputNum.split()
res = [int(i) for i in num_list]
sum = 1

for i in range(0, len(res)):
    if res[i]%2:
        sum*=res[i]
print(sum)