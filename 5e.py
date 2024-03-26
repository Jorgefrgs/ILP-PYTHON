matriz = []
orc = 0
humano = 0
for _ in range(10):
    matriz.append(input().split())
tem_mago_no_lado_orc = any('m' in matriz[i][:5] for i in range(10))
tem_mago_no_lado_humano = any('m' in matriz[i][5:] for i in range(10))
for i in range(10):
    for j in range(5):
        if matriz[i][j] in ['o','m']:
            orc += 1
for i in range(10):
    for j in range(5, 10):
        if matriz[i][j] in ['h','m']:
            humano += 1
if tem_mago_no_lado_orc:
    for i in range(10):
        for j in range(5):
            if matriz[i][j] != "*":
                if j > 0 and matriz[i][j - 1] in ['m', 'o']:
                    orc += 1
                if j < 4 and matriz[i][j + 1] in ['m', 'o']:
                    orc += 1
                if i > 0 and matriz[i - 1][j] in ['m', 'o']:
                    orc += 1
                if i < 9 and matriz[i + 1][j] in ['m', 'o']:
                    orc += 1
if tem_mago_no_lado_humano:
    for i in range(10):
        for j in range(5, 10):
            if matriz[i][j] != "*":
                if j > 5 and matriz[i][j - 1] in ['m', 'h']:
                    humano += 1
                if j < 9 and matriz[i][j + 1] in ['m', 'h']:
                    humano += 1
                if i > 0 and matriz[i - 1][j] in ['m', 'h']:
                    humano += 1
                if i < 9 and matriz[i + 1][j] in ['m', 'h']:
                    humano += 1
if orc > humano:
    print("Loktar Ogar!!!")
elif humano > orc:
    print("Pela Alianca!")
else:
    print("Batalha lendaria!")