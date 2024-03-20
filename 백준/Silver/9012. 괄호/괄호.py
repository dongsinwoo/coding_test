import sys 


def search (bracket):
    bracket_list = list(bracket)
    stack_list = []

    for b in bracket_list:
        if b == "(":
            stack_list.append(b)
        elif b == ")" and not stack_list :
            return "NO"
        elif b == ")":
            stack_list.pop()
        
    if not stack_list:
        return "YES"
    else:
        return "NO"

        

input = sys.stdin.readline
n = int(input())
result = []
for _ in range(n):
    brackets = input().strip()
    print(search(brackets))