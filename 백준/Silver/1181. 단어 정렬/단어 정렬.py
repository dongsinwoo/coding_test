n = int(input())
result = []
for _ in range(n):
    string = input()
    if [len(string),string] in result:
        continue
    stringList = [len(string),string]
    result.append(stringList)

result.sort(key = lambda x: (x[0],x[1]))

for str in result:
    print(str[1])