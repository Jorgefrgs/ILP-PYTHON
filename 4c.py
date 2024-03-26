n = int(input())
lista = []
duplice = []
tem_duplice = False
for i in range(1):
    lista.extend(map(int,input().split()))
    for p in lista:
        if lista.count(p) > 1:
            duplice.append(p)
            tem_duplice = True
if tem_duplice == True:
    print(duplice[0])
else:
    print("-1")