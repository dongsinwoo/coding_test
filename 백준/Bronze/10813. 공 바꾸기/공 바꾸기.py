n, m = map(int, input().split(" "))

arr = []
result = ""

for num in range(1,n+1):
    arr.append(num)


for i in range(0, m):
    a,b = map(int, input().split(" "))
    changeA = arr[a-1]
    changeB = arr[b-1]

    arr[a-1] = changeB
    arr[b-1] = changeA


for i in range(0,n):
    result += str(arr[i]) + " "

print(result)
