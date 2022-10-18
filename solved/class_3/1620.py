import sys


N, M = map(int, sys.stdin.readline().rstrip().split(" "))
pokemon_list = dict()
for i in range(1, N +1):
    pokemon = sys.stdin.readline().rstrip()
    pokemon_list[str(i)] = pokemon
    pokemon_list[pokemon] = str(i)
for _ in range(M):
    input_value = sys.stdin.readline().rstrip()
    print(pokemon_list[input_value])