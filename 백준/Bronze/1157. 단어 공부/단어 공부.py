chr = input().upper()
count_dict = {}
max_count = 0
result = []

for char in chr:
    count_dict[char] = count_dict.get(char, 0) + 1
    if count_dict[char] > max_count:
        max_count = count_dict[char]
        result = [char]
    elif count_dict[char] == max_count:
        result.append(char)

if len(result) >= 2:
    print("?")
else:
    print(result[0])