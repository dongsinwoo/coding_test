test_num = int(input())

def result():
    amount = int(input())
    quarter = amount // 25
    amount = amount % 25
    dime = amount // 10
    amount = amount % 10
    nickel = amount // 5
    amount = amount % 5
    penny = amount // 1
    return print(quarter, dime, nickel, penny)
    


for _ in range(0,test_num):
    result()