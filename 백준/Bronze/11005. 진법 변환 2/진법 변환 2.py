from string import ascii_uppercase

n,q = map(int,input().split(" "))
strList = "0123456789"+str(ascii_uppercase)
def solution(n, q):
    rev_base = ''

    while n > 0:
        n, mod = divmod(n, q)
        rev_base += strList[mod]

    return rev_base[::-1]
    # 역순인 진수를 뒤집어 줘야 원래 변환 하고자하는 base가 출력
    
print(solution(n, q))