a, b = input().split()
b = int(b)
if a == "N":
    b = 0
    print("Acesso permitido!")
elif a == "S" and b >= 30:
    print("Imune! Siga para um local seguro")
elif a == "S" and b >= 7:
    print("Acesso negado! Fique em observacao")
else:
    print("Acesso negado! Isolamento urgente")