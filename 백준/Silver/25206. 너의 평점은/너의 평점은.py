ratingObject = {
    "A+" : 4.5,
    "A0" : 4.0,
    "B+" : 3.5,
    "B0" : 3.0,
    "C+" : 2.5,
    "C0" : 2.0,
    "D+" : 1.5,
    "D0" : 1.0,
    "F" : 0
}
result = 0
div = 0
for num in range(0,20):
    subject, majorScore, Rating = input().split(" ")
    
    if Rating != "P":
        div += float(majorScore)
        result += ratingObject[Rating] * float(majorScore)


print(result/div)