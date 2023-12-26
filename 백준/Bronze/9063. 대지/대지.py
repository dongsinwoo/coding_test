n = int(input())
x_list = []
y_list = []
for _ in range(n):
    x,y = map(int, input().split())
    x_list.append(x)
    y_list.append(y)

x_line = max(x_list)-min(x_list)
y_line = max(y_list)-min(y_list)
area = x_line * y_line

print(area)