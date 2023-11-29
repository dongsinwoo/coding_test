n,x = map(int, input("").split(" "))
a = list(map(int, input("").split(" ")))
result = ""
for i in range(0,n):
    if(a[i] < x):
        result += str(a[i]) + " "
        
print(result)