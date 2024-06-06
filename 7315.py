from fractions import Fraction
nums = input()
num_list = nums.split()
res = [int(i) for i in num_list]
a = res[0]
b = res[1]
q = Fraction(a, b)
print (f'{q}')