n,m = map(int,input().split())
matriz = []
teste = 0
for i in range(n):
    matriz.append(list(map(int,input().split())))
for j in range(n):
    for k in range(m):
        if matriz[j][k] == 0:
            teste += 1
            if matriz[j-1][k] == 1:
                teste += 1
            if matriz [j+1][k] == 1:
                teste += 1
            if matriz [j][k-1] == 1:
                teste += 1
            if matriz [j][k+1] == 1:
                teste += 1
                if teste == 5:
                    print(j, k)
                else:
                    print("0", "0")