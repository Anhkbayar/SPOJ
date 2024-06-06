inputNum = input()
num_list = inputNum.split()
res = [int(i) for i in num_list]
equals_list = []

for i in range(0, len(res)):
    if res[i]%3 == 0:
        equals_list.append(res[i])

print(len(equals_list))