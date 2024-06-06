sn= input()
num = int(input())
res = [int(i) for i in sn.split()]
floor = res[0]
ail = res[1]

if num%ail == 0:
    print(int(num/ail), ail)
else:
    print(int((num/ail)+1), num%ail)