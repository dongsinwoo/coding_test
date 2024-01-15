from itertools import *

allLen, answer = map(int, input().split())
cardList = map(int, input().split())
cases = list(combinations(cardList,3))
result = []
for card in cases:
    number_sum = sum(card)
    if answer >= number_sum:
        result.append(number_sum)

print(max(result))
