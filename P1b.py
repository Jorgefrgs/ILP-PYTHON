d, e = map(int,input().split())
for i in range(d):
    a = int(input())
    e -= a
    if e <= 0:
        print(i+1)
        break
if e > 0:
    print("Resistiu")