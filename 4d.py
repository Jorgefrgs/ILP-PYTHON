s, n = map(int, input().split())
pedras = [0] * n
for i in range(s):
    p = int(input())
    for j in range(0, n, p):
        pedras[j] = 1
print(' '.join(map(str, pedras)))