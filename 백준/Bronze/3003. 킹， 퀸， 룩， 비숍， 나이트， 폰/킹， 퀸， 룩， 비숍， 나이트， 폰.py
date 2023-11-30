userChessList = list(map(int, input().split(" ")))
chessPiceCount = [1,1,2,2,2,8]
result = ""

for index in range(0,len(userChessList)):
    difference =  userChessList[index] - chessPiceCount[index]
    if difference == 0:
        result += str(difference) + " "
    elif difference > 0:
        result += str(-difference) + " "
    elif difference < 0:
        result += str(-difference) + " "

print(result)