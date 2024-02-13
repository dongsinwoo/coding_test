sang_card_lang = int(input())
sang_card_list = list(map(int, input().split()))
result_card_lang = int(input())
result_card_list = list(map(int,input().split()))
result_dic = {key:0 for key in result_card_list}

for card in sang_card_list:
    if card in result_dic:
        result_dic[card]+=1

for card in result_card_list:
    print(result_dic[card])