n = int(input())

if(n % 5 == 0):
    print(n // 5)
else:
    result = 0
    while n > 0:
        n -= 3
        result += 1

        if n % 5 == 0:
            result += n//5
            print(result)
            break
        if n == 1 or n == 2:
            print(-1)
            break
        if n == 0:
            print(result)
            break
