e, p = map(int, input().split())
ataques = 0
for p in range(p, 0, -1):
    e -= p
    ataques += 1
    if e <= 0:
        print(ataques)
        break
else:
    print('F')