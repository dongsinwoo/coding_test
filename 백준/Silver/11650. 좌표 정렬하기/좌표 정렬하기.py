n = int(input())
answer = []
for _ in range(n):
    coordinate = list(map(int, input().split()))
    answer.append(coordinate)

for x,y in sorted(answer):
    print(x,y)