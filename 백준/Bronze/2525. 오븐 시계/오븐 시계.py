a, b = map(int,input("").split(" "))
c = int(input(""))

resutl = a * 60 + b + c
h = resutl // 60
m = resutl % 60 
if (h >=24):
    h -= 24
    print(f"{h} {m}")
else:
    print(f"{h} {m}")