def funcao(matriz, p):
    qtd = 0
    for t in matriz:
        for pokemon in t:
            if pokemon == p:
                qtd += 1
    return qtd
n, m = map(int, input().split())
matriz = []
for i in range(n):
    t = list(map(int, input().split()))
    matriz.append(t)
p = int(input())
qtd_poke = funcao(matriz, p)
print("Ash pegou", qtd_poke, "pokemon")