import sys

input = sys.stdin.readline

n, m = map(int, input().split())

result_dic = {}
result = []
for _ in range(n):
    person = input()
    result_dic[person] = 0
    

for _ in range(m):
    person = input()
    if person in result_dic:
        result.append(person.rstrip())

print(len(result))
for person in sorted(result):
    print(person)