def nemeh(n, times):
    result = 0
    for _ in range(times):
        result += n
    return result

n = 100 
times = int(input()) 

result = nemeh(n, times)
print(result)
