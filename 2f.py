a, m, c = map(int,input().split())
if a // 2 <= m // 3 and a // 2 <= c // 5:
    espadas = a // 2
elif m // 3 <= a // 2 and m // 3 <= c // 5:
    espadas = m // 3
else:
    espadas = c // 5
print(espadas)