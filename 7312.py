def find_factorial_number(n):
    if n < 1:
        return "No"
    
    factorial = 1
    i = 1
    while factorial <= n:
        if factorial == n:
            return i
        i += 1
        factorial *= i
    
    return "No"

number = int(input())
print(find_factorial_number(number))
