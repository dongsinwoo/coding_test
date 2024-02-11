import sys
n = int(sys.stdin.readline().strip())
x_list = list(map(int, sys.stdin.readline().strip().split()))
s_x_list = list(set(x_list))
s_x_list.sort()
x_index = [x for x in range(len(s_x_list))]
x_dic = {key:value for key, value in zip(s_x_list,x_index)}
for x in x_list:
    print(x_dic[x])

