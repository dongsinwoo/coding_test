import sys
input=sys.stdin.readline
n = int(input())
result = []
for _ in range(n):
    result.append(int(input()))

for num in sorted(result):
    print(num)