n,m = map(int, input().split())
arr1 = []
arr2 = []
result = ""
for num in range(0,n):
    row = list(map(int, input().split()))
    arr1.append(row)

for num in range(0,n):
    row = list(map(int, input().split()))
    arr2.append(row)

for leng in range(0,n):
    
    for index in range(0,m):
        result += str(arr1[leng][index] + arr2[leng][index]) + " "
    
    result += "\n"

print(result)