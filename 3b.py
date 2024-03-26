n = int(input())
geleia = 0
semgeleia = 0
for i in range(n):
    codigo = int(input())
    if codigo == 10:
        geleia += 1
    elif codigo == 11:
        semgeleia += 1
if geleia > semgeleia:
    print("Tradicional")
else:
    print("Geleia")