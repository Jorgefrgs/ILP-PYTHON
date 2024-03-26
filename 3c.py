n = int(input())
maior = -1
for i in range(n):
    p = int(input())
    if p > maior:
        maior = p
print(maior)