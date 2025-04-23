import sys
input = sys.stdin.readline

n, m = map(int, input().split())

dic = {}

for _ in range(n):
    word = input().strip()
    if len(word) < m:
        continue
    if word in dic:
        dic[word] += 1
    else:
        dic[word] = 1

# 정렬 기준:
# 1. 자주 등장하는 단어 우선 (-빈도)
# 2. 길이가 긴 단어 우선 (-길이)
# 3. 사전 순
sorted_words = sorted(dic.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

for word, _ in sorted_words:
    print(word)