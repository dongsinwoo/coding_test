def solution(number, limit, power):
    soldier_list = [0] * number

    for i in range(number):
        num = i+1
        soldier_power = 0
        for j in range(1, int(num**(1/2)) + 1):
            if (num % j == 0):
                soldier_power+=1 
                if ( (j**2) != num): 
                    soldier_power+=1 
        
        if soldier_power > limit:
            soldier_list[i] = power
        else:
            soldier_list[i] = soldier_power

    return sum(soldier_list)