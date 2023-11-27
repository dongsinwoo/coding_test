h, m = map(int,input("").split(" "))

hResult = h
mResult = m - 45

if mResult < 0:
    hResult -=1
    if hResult < 0 :
        hResult+= 24
    
    mResult += 60
    print(f"{hResult} {mResult}")
else:
    print(f"{hResult} {mResult}")