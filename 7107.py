inputNum = input()
num_list = inputNum.split()
res = [int(i) for i in num_list]
sum = 0

for i in range(0, len(res)):
    if res[i]%2 == 0:
        sum+=res[i]
print(sum)