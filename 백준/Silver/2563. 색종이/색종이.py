paper = int(input())

# 백그라운드 생성
background = [[0]*101 for i in range(101)]


for _ in range(0,paper):
    x, y = map(int, input().split(" "))

    for i in range(0,10):
        for j in range(0,10):
            background[y+i][x+j] = 1

result = 0
    
for row in background:
    result += row.count(1)

print(result)