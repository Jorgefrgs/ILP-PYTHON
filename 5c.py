n = int(input())
matriz = []
contador1 = 0
contador2 = 0
for i in range(n):
    matriz.append(list(map(int,input().split())))
x, y = map(int,input().split())
for j in range(n):
        contador2 += matriz[j][y]
if y < x:
    contador2 -= matriz[x][y]
for k in range(n):
        contador1 += matriz[x][k]
if x <= y:
    contador1 -= matriz[x][y]
print(f'Harry {contador1}')
print(f'Ron {contador2}')