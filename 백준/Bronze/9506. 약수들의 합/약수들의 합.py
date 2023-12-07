while True:
    n = int(input())
    result = 0
    arr = []
    if n == -1:
        break
    else:
        for num in range(1, n):
            if n % num == 0:
                arr.append(num)
                result += num

        if result == n :
            resultStr = f"{result} = "
            for i, num in enumerate(arr):
                resultStr += str(num)
                if i < len(arr) - 1:
                    resultStr += " + "
            print(resultStr)
        else:
            print(f"{n} is NOT perfect.")
    


        
