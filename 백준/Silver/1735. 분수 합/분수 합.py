import math
a1,a2 = map(int, input().split())
b1,b2 = map(int,input() .split())

if a2 == b2:
    result1 = a1 + b1
    result2 = a2
else:
    result1 = a1*b2 + b1* a2
    result2 = a2*b2



i = math.gcd(result1,result2)

if result2 % i == 0 and result1 % i == 0:
    result1 = result1 // i
    result2 = result2 // i

print(result1, result2)