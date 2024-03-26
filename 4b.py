n = int(input())
flista = []
for i in range(1):
    f = map(int,input().split())
    flista.extend(f)
flista.reverse()
for j in range(n):
    print(f'{(n-j)}: {flista[j]}')