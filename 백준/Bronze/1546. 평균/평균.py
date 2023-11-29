n = int(input())

subject = list(map(int,input().split(" ")))
max_score = max(subject)
result = 0

for index in range(0,n):
    result += subject[index]/max_score * 100

print(result/n)