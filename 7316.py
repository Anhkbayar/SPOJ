def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def find_lcm(a, b, c):
    gcd = find_gcd(a, b)
    lcm = (a * b) // gcd
    gcd = find_gcd(lcm, c)
    lcm = (lcm * c) // gcd
    return lcm

inputNum = input()
num_list = inputNum.split()
res = [int(i) for i in num_list]

a = res[0]
b = res[1]
c = res[2]
print(find_lcm(a,b,c))