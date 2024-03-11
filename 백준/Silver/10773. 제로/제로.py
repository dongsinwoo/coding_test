import sys

k = int(sys.stdin.readline())
save = []
for _ in range(k):

    insert = int(sys.stdin.readline())

    if insert == 0 :
        save.pop()
    else:
        save.append(insert)

print(sum(save))