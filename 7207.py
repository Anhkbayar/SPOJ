def nemeh(n, times):
    result = 0
    for _ in range(times):
        result += n
    return result
inputNum = input()
num_list = inputNum.split()
res = [int(i) for i in num_list]

a = num_list[0]
n = num_list[1]

result = nemeh(a, n)
print(result)