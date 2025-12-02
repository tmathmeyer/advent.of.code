
F = 'real.input'
D = 50
C = 0
with open(F) as f:
  for l in f.readlines():
    V = (-1 if l[0]=='L' else 1) * int(l[1:])
    if V > 0:
      C += V//100
      D += V - (V//100) * 100
      if D > 99:
        C += 1
      D = D % 100
    elif V < 0:
      C -= ((V // 100) + 1)
      SZ = D == 0
      D += ((V%100) - 100)
      if D < 1 and not SZ:
        C += 1
      D = D % 100


print(C)
