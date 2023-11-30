word = input()
dial = ["0","1","ABC","DEF","GHI","JKL","MNO","PQRS","TUV","WXYZ","0"]
result = 0

for index in range(0, len(word)):

    for i in range(0,len(dial)):

        if dial[i].find(word[index]) != -1:
            result += i+1


print(result)