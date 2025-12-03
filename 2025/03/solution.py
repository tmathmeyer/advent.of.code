
INPUT = 'real.input'


def p4(L, M):
  DM = {d:[] for d in range(10)}
  for I,D in enumerate(L):
    DM[int(D)].append(I)
  R = []
  LP = -1
  while len(R) < M:
    MP = len(L) - M + len(R)
    for d in [9,8,7,6,5,4,3,2,1]:
      if DM[d] and LP < DM[d][0] <= MP:
        LP = DM[d].pop(0)
        R.append(d)
        break
    for d in [9,8,7,6,5,4,3,2,1]:
      while DM[d] and DM[d][0] < LP:
        DM[d].pop(0)
  return int(''.join(str(d) for d in R))


with open(INPUT, 'r') as f:
  sum = 0
  for x in f.readlines():
    sum += p4(x.strip(), 12)
  print(sum)
