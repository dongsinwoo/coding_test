import sys

input = sys.stdin.readline

n = int(input())
n_list = list(map(int, input().split()))

result_dic = {}

for num in n_list:
    
    if num in result_dic:
        result_dic[num] += 1
    else: 
        result_dic[num] = 1

m = int(input())
m_list = list(map(int, input().split()))

for num in m_list:
    if num in result_dic:
        print(result_dic[num])
    else: 
        result_dic[num] = 0
        print(result_dic[num])
