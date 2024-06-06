def gcd(a, b):
    if a == 0:
        return b
 
    return gcd(b % a, a)
nums = input()
num_list = nums.split()
res = [int(i) for i in num_list]
i = res[0]
j = res[1]
print(gcd(i, j))