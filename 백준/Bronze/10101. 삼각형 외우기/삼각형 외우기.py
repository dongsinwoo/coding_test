x = int(input())
y = int(input())
z = int(input())
arr = [x,y,z]

if sum(arr) == 180:
    result = len(set(arr))
    if result == 3:
        print("Scalene")
    elif result == 2:
        print("Isosceles")
    elif result == 1:
        print("Equilateral")
else:
    print("Error")