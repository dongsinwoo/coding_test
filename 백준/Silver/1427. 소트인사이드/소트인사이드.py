import sys
input = sys.stdin.readline
n = input()
result = []
answer = ""
for chr in n:
    result.append(chr)

 

for chr in sorted(result)[::-1]:
    answer += chr

print(int(answer))