test = int(input())
result = ""
for num in range(1,test+1):
    result = " " * (test-num) +"*" * (num*2-1)
    print(result)

for num in range(test-1, 0,-1):
    result = " " * (test-num) +"*" * (num*2-1)
    print(result)