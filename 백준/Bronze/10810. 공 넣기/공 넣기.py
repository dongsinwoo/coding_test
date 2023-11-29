n, m = map(int,input("").split(" "))

arr = []
result = ""

for i in range(0, n):
    arr.append(0)


for i in range(0,m):
    i, j, k = map(int,input("").split(" "))
    for number in range(i-1,j):
        arr[number] = k


for index in range(0,n):
    result += str(arr[index]) + " "

print(result)