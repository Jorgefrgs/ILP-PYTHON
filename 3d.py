t = int(input())
p = int(input())
while p != 0:
    p = int(input())
    if p > t:
        print("ALARME")
        break
    if p <= t:
        continue
if p == 0:
    print("O Havai pode dormir tranquilo")