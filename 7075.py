def cube(n):
    if n == 0:
        return 0
    else:
        return cube(pow(n,3))+ cube(pow(n-1,3))
num = int(input())
print(cube(num))
