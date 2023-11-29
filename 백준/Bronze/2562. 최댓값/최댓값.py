arr = []
for i in range(1,10):
    n = int(input(""))
    arr.append(n)

max_value = max(arr)
max_value_index = arr.index(max_value)
print(max_value)
print(max_value_index+1)