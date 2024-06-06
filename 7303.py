n = input()
num_list = list(map(int, n))
sum = 0
for i in num_list:
    if i%2==0:
        sum+=i
print(sum)