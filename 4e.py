n = int(input())
xlista = []
xlista.extend(map(int, input().split()))
m = int(input())
mfinal = m
for i in xlista:
    if i == 0:
        continue
    elif i == 1:
        mfinal = m
    else:
        mfinal -= i
        if mfinal <= 0:
            print("You Died")
            break
if mfinal > 0:
    print("Yes, you can")