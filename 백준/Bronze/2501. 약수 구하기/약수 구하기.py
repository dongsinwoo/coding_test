a,b = map(int, input().split(" "))
arr = []
for num in range(1, a+1):
    if a % num == 0:
        arr.append(num)
    
if len(arr) >= b:
    print(arr[b-1])
else:
    print(0)