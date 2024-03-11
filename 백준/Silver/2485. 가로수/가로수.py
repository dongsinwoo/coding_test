import sys
from math import gcd

n = int(sys.stdin.readline())
# 첫 번째 가로수 (시작 기준 가로수)
a = int(sys.stdin.readline())

# 간격을 담아줄 리스트
arr = []
for _ in range(n-1):

    garosu_num = int(sys.stdin.readline())
    # 현재 가로수 사이의 간격
    arr.append(garosu_num - a)
    a = garosu_num

# 간격간의 최소 공약수를 구하기
g = arr[0]

for i in range(1,len(arr)):
    g = gcd(g,arr[i])

answer = 0 

for each in arr:
    answer += each // g - 1

print(answer)    
