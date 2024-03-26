f, c = map(int,input().split())
matriz = []
for i in range(f):
    x = list(map(int,input().split()))
    matriz.append(x)
for j in range(len(matriz)):
    for k in range(len(matriz[i])):
        if j < f and k < (c-1):
            if matriz[j][k] == 0 and matriz[j][k+1] == 0:
                print(f'Fileira: {j+1}')
                print(f'Assentos: {k+1} e {k+2}')
                break