n = int(input(""))

for index in range(1, n+1, 1):
    a,b = map(int, input("").split(" "))
    
    print(f"Case #{index}: {a} + {b} = {a+b}")