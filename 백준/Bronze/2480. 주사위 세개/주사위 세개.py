a, b, c = map(int, input("").split(" "))

result1 = a == b == c
result2 = a != b and b !=c and a != c
result3 = a == b != c
result4 = a != b == c
result5 = a == c != b

if(result1):
    print(10000 + (1000 * a))
elif(result2):
    max_value = max(a, b, c)
    print(max_value*100)
elif(result3):
    print(1000 + (100 * a))
elif(result4):
    print(1000 + (100 * b))
elif(result5):
    print(1000 + (100 * a))
