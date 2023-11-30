test_case = int(input())

for testNum in range(0,test_case):
    num, chr = input().split(" ")
    result = ""
    for i in range(0,len(chr)):
        result += chr[i] * int(num)
    
    print(result)