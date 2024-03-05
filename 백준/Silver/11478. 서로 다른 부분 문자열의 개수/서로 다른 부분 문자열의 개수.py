word = input()
result = 0

def sub_chr(word_x, num):
    sets = set()

    for i in range(len(word_x)-(num - 1)):
        sets.add(word_x[i : i+num])
    
    return sets


for i in range(len(word)):
    result += len(sub_chr(word, i+1))

print(result)