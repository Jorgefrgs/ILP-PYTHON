n = int(input())
lista = list(map(int,input().split()))
c = int(input())
if c in lista:
    cont = lista.count(c)
    print(sum(lista) - (c * cont + c * cont))