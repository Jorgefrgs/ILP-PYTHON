n = int(input())
nx = map(int,input().split())
c = int(input())
ne = []
for i in nx:
    ne.append(i)
if c in ne:
    print(c)
else:
    print("-1")