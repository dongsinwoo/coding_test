def censorship(bracket):
    return [brac for brac in bracket if brac in ["(", ")", "[", "]"]]

def stack_result(cb):
    stack_list = []
    for b in cb:
        if b in ["(", "["]:
            stack_list.append(b)
        elif b in [")", "]"] and (not stack_list or (b == ")" and stack_list[-1] != "(") or (b == "]" and stack_list[-1] != "[")):
            return "no"
        else:
            stack_list.pop()
    return "yes" if not stack_list else "no"

comands = ""
while True:
    brackets = input()
    if brackets == ".":
        break
    comands += brackets

comands_list = comands.split(".")
comands_list.pop()
for ls in comands_list:
    b_c = censorship(ls)
    print(stack_result(b_c))
