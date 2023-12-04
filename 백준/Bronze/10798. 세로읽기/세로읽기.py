test_num = 5
arr = []
maxLeng = 0
result = ""
for num in range(0,test_num):
    word = input()
    wordLen = len(word)
    arr.append(word)
    if maxLeng < wordLen:
        maxLeng = wordLen


for index in range(0,maxLeng):
    for word in arr:
        if len(word) <= index:
            continue
        else:
            result += word[index]

print(result)