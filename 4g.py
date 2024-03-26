n = int(input())
assassinatos = list(map(int, input().split()))
maior = max(assassinatos)
contador = [0] * (maior + 1)
for assassinato in assassinatos:
    contador[assassinato] += 1
for i in range(maior + 1):
    for j in range(contador[i]):
        print(i, end=' ')
print()