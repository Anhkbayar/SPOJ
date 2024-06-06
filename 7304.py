n = input()
num_list = list(map(int, n))
sum = 0
for i in num_list:
    if i%2:
        sum+=1
print(sum)