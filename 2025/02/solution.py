import math

def nsn1(x):
  d = 1 if x == 0 else int(math.log(x, 10)) + 1
  z = 10 ** (d//2)
  if d%2 == 1:
    return z*(z*10+1)
  l = x % z
  u = (x - l) // z
  if l < u:
    return u * (z + 1)
  if u == z - 1:
    return (u + 1) * (z*10 + 1)
  return (u + 1) * (z + 1)

def nsn2(x):
  if x == 0:
    return 11
  x += 1
  d = int(math.log(x+1, 10)) + 1
  z = 10 ** (d//2)
  if x == z - 1:
    x += 1
    d += 1
  nxt = x*10
  for rs in range(1, d):
    if d%rs == 0:
      c = d//rs
      p = x // (10 ** (d - rs))
      g = 10 ** rs
      for i in range(2):
        p = p + i
        if p == g:
          g *= 10
        vv = 0
        for _ in range(c):
          vv *= g
          vv += p
        if nxt > vv >= x:
          nxt = vv
  return nxt

def gafr(s,e,fn):
  s,e = int(s)-1,int(e)
  while s <= e:
    s = fn(s)
    if s <= e:
      yield s

def rl(f, fn):
  sum = 0
  with open(f, 'r') as i:
    for rg in i.read().strip().split(','):
      for s in gafr(*rg.split('-'), fn):
        sum += s
  return sum

#print(rl('real.input', nsn1))
print(rl('real.input', nsn2))