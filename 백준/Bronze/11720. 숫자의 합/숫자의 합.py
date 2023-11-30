chrIndex = int(input())
chrList = input()
result = 0

for i in range(0,chrIndex):
    result += int(chrList[i])
    
print(result)