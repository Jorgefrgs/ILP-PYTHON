q1, q2, q3 = input().split()
e1, e2, e3 = input().split()
q1, q2, q3 = int(q1), int(q2), int(q3)
e1, e2, e3 = int(e1), int(e2), int(e3) 
totalq = q1 + q2 + q3
totale = e1 + e2 + e3
perde = totale + (totale * 2)
final = totalq - perde
print(final)