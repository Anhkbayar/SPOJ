inputNum = input()
num_list = inputNum.split()
res = [int(i) for i in num_list]

num = num_list[0]
dig = res[1]

numto = list(map(int, num))
n=0
for i in numto:
    if i == dig:
        n+=1
print(n)






