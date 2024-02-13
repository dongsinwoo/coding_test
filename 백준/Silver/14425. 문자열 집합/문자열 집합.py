n,m = map(int, input().split())
s_list = []
m_list = []
result = 0
for _ in range(n):
    s_list.append(input())

for _ in range(m):
    m_list.append(input())

for s in s_list:    
    result += m_list.count(s)

print(result)