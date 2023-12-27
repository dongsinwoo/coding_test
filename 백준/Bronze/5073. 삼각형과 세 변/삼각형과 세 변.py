while True:
    inputList = list(map(int,input().split()))

    if sum(inputList) == 0:
        break
    
    inputList.sort()
    condition = inputList[0] + inputList[1] <= inputList[2]
    
    if condition:
        print("Invalid")
        continue
    else:
        setInputList = set(inputList)
        lenSetInputList = len(setInputList)
        if lenSetInputList == 2:
            print("Isosceles")
        elif lenSetInputList == 1:
            print("Equilateral")
        else:
            print("Scalene")