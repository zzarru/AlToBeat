pokemon_numkey_dict = {}
pokemon_strkey_dict = {}
N, M = map(int,input().split())

for i in range(1,N+1):
    temp = input()
    pokemon_numkey_dict[str(i)] = temp
    pokemon_strkey_dict[temp] = str(i)

for _ in range(M):
    key = input()
    if key in pokemon_numkey_dict:
        print(pokemon_numkey_dict[key])
    else:
        print(pokemon_strkey_dict[key])