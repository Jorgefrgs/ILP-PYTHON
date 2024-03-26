n1, n2, n3, n4, n5, n6 = map(int,input().split())
nota = n1 + n2 + n3 + n4 + n5 + n6
if nota >= 250:
    print("S+")
elif nota >= 200:
    print("S")
elif nota >= 180:
    print("S-")
elif nota >= 150:
    print("A+")
elif nota >= 100:
    print("A")
elif nota >= 80:
    print("A-")
elif nota >= 60:
    print("B+")
elif nota >= 40:
    print("B")
elif nota <= 39:
    print("B-")