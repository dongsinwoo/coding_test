def find_fraction(x):
    line = 1
    while x > line:
        x -= line
        line += 1

    if line % 2 == 0:
        numerator = x
        denominator = line - x + 1
    else:
        numerator = line - x + 1
        denominator = x

    return f"{numerator}/{denominator}"

x = int(input())
result = find_fraction(x)
print(result)
