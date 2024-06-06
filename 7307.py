num = input()
numto = list(map(int, num))
def largest(arr, n):
    mx = arr[0]
    for i in range(1, n):
        if arr[i] < mx:
            mx = arr[i]
 
    return mx
print(largest(numto, len(numto)))








