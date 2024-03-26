n = int(input())
pesos = []
peso_total = 0
for i in range(n):
    s, k = input().split()
    k = int(k)
    pesos.append(k)
    if k in pesos:
        peso_total += k
c = int(input())
if peso_total <= c:
    print("Vamos todos encontrar a montanha!")
else:
    print("Vamos virar almoço de aranhas gigantes!")