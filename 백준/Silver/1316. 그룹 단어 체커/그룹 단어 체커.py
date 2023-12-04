test_num = int(input())
result = 0

def is_group(word):
    set_chr = set()
    prve_char = ""
    for chr in word:
        if chr == prve_char:
            continue
        if chr in set_chr:
            return False
        set_chr.add(chr)
        prve_char = chr
    return True

for num in range(0, test_num):
    word = input()
    returnResult = is_group(word)
    if returnResult:
        result += 1
    

print(result)