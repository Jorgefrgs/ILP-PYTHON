n = int(input())
nivel = 1
for i in range(n):
  evento, acao = input().split()
  acao = int(acao)
  if evento == "t":
    nivel += acao
  elif evento == "m":
    print("Combate iniciado")
    if nivel >= acao:
      print("VITORIA")
      nivel += 1
    else:
      print("Derrota! Fim da aventura")
      break
  elif evento == "b":
    nivel -= acao
  if nivel >= 5:
    print("Aventura concluida")
    break
  if nivel < 1:
    nivel = 0
    continue
print()