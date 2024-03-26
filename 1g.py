n = int(input())
hora = int(n / 3600)
nresto = n % 3600
minuto = int(nresto / 60)
segundo = n % 60
print(f'{hora}h {minuto}m {segundo}s')