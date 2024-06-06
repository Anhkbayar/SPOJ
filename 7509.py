n = int(input())
nums = input()
search = int(input())
num_list = [int(i) for i in nums.split()]

for i in range(0, n):
    if num_list[i] == search:
        print("YES")
        break
    else:
        print("NO")
        break
    
