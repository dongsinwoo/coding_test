n = int(input())
answer = []
for _ in range(n):
    coordinate = list(map(int, input().split()))
    answer.append(coordinate)

answer.sort(key=lambda x:(x[1],x[0]))

for x,y in answer:
    print(x,y)