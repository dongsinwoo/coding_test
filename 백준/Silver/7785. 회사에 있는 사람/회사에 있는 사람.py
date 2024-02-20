import sys
input = sys.stdin.readline
n = int(input())
result = set()
for _ in range(n):
    name, work = map(str,input().rstrip().split())
    if work == "enter":
        result.add(name)
    elif work == "leave":
        result.remove(name)

for name in sorted(result,reverse=True):
    print(name)