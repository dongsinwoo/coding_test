start = int(input())
end = int(input())
resultList = []
result = 0
for num in range(start, end+1):
    arr = []
    for i in range(1,num+1):
        if num % i == 0:
            arr.append(i)
    
    if len(arr) == 2:
        resultList.append(num)


for num in resultList:
    result+=num

if len(resultList) == 0:
    print(-1)
else:
    print(result)
    print(resultList[0])