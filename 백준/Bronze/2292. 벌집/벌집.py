room = int(input())

if room == 1:
    print(room)
else:
    start, end = 2, 7
    num = 1

    while not (start <= room <= end):
        start, end = end, end + 6 * (num + 1)
        num += 1

    print(num + 1)
