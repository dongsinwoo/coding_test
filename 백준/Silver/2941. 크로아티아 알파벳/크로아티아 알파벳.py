alpabet = input()
croatiaAlpabet = ["c=","c-","dz=","d-","lj","nj","s=","z="]


for char in croatiaAlpabet:
    count = alpabet.count(char)

    if count > 0:
        alpabet = alpabet.replace(char,"a")
    

print(len(alpabet))