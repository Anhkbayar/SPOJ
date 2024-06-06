def is_power_of_two(n):
    if n > 0 and (n & (n - 1)) == 0:
        return "YES"
    else:
        return "NO"
number = int(input())
print(is_power_of_two(number))
