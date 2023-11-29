n,m = map(int, input('').split(" "))

arr = []
result = ""

for i in range(1,n+1):
    arr.append(i)

for i in range(0,m):
    a,b = map(int, input("").split(" "))
    start = a-1
    end = b
    reverseList = arr[start:end][::-1]
    arr[start:end] = reverseList


for i in range(0,n):
    result += str(arr[i]) + " "

print(result)