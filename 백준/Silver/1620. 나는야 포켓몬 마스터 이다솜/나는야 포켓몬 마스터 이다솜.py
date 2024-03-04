import sys
n, m = map(int, sys.stdin.readline().split())
pokemon_list = {}

# 포켓몬 개수
for _ in range(1,n+1):

    pokemon = sys.stdin.readline().rstrip()
    pokemon_list[_] = pokemon
    pokemon_list[pokemon] = _
    

# 문제 개수
for _ in range(m):

    quiz = sys.stdin.readline().rstrip()

    if quiz.isdigit():
        print(pokemon_list[int(quiz)])
        
    else :
        print(pokemon_list[quiz])