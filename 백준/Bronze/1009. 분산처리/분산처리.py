t =  int(input())

for n in range(t):
    a,e = map(int, input().split(" "))
    
    if (a % 10 == 0):
         print(10)
    else:
        e = (e%4) +4
        print((a**e) %10)
        
