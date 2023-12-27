input_list = list(map(int,input().split()))
input_list.sort()


condition = input_list[0] + input_list[1] <= input_list[2]
while condition:
    condition = input_list[0] + input_list[1] < input_list[2]
    input_list[2] -= 1

print(sum(input_list))