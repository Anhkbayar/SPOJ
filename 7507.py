size = int(input())
nums = input()
num_list = [int(i) for i in nums.split()]
maxi = max(num_list)
for i in range(0, size):
    if maxi == num_list[i]:
        print(f"{maxi} {i+1}")
        break