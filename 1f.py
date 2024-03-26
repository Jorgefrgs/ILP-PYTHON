n, xp = map(int, input().split())
xpiY, xpiL, xpiA = map(int, input().split())
new_xpiY = xpiY + n * xp
new_xpiL = xpiL + n * xp 
new_xpiA = xpiA + n * xp
print("Yoda", new_xpiY)
print("Luke", new_xpiL)
print("Ahsoka", new_xpiA)