z, g = input().split()
d, c = input().split()
if z != d:
    print("Bloqueado")
else:
    print("Driblado")
if z == d and g != c:
    print("...e o goleiro pega")
elif z == d and g == c:
    print("Gol")