n = int(input())
soma = 0
for i in range(n):
    soma += int(input())
if soma > 5/10 * n:
    print('Regiao com alto indice de perda de biodiversidade')
if soma < 3/10 * n:
    print('Regiao segura')
if 3/10 * n < soma <= 5/10 * n:
    print('Regiao em estado de alerta')