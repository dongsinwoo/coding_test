num = int(input())

for n in range(1,num+1):
    list_num = sum(map(int, str(n)))
    if n + list_num == num:
        print(n)
        break
    if n == num :
        print(0)
