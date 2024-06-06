inputNum = input()
num_list = inputNum.split()
res = [int(i) for i in num_list]
res.sort()
base = res[0]
opp = res[1]
hypp = res[2]
hyppc = pow(hypp, 2)
basec = pow(base, 2)+ pow(opp, 2)
if hyppc == basec:
    print("Right")
elif hyppc > basec:
    print("Obtuse")
else:
    print("Acute")

    

