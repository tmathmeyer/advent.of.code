
import sys
from functools import reduce

f = {'*': int.__mul__, '+': int.__add__}
r = reduce

def p1(L):
  # fuckin lol
  print(r(f['+'], [r(f[o],map(int,n)) for *n,o in zip(*[l.split() for l in L])]))


def p2(L):
  M = max(len(l) for l in L)
  S,O,R = 0,None,[]
  for l in zip(*[l + ' ' * (M - len(l)) for l in L]):
    n,o = ''.join(l[:-1]).strip(),l[-1].strip()
    if not n:
      S += reduce(O,R)
      O,R = None,[]
      continue
    if o: O = f[o]
    R.append(int(n))
  print(S)


with open(sys.INPUTFILE, 'r') as file:
  L = list(file.readlines())
  p1(L)
  p2(L)


