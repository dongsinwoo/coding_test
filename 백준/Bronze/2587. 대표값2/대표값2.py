result = []
for _ in range(5):
    num = int(input())
    result.append(num)

print(sum(result) // len(result))
print(sorted(result)[2])
