
import sys

def ar(r, s, e):
  nr = []
  os = None
  oe = None
  a = False
  for S,E in r:
    if a:
      nr.append((S,E))
      continue
    if os and e < S:
      nr.append((os, oe))
      nr.append((S, E))
      os = None
      a = True
      continue
    if os and e <= E:
      nr.append((os, E))
      os = None
      a = True
      continue
    if os and e > E:
      continue
    if s > E:
      nr.append((S,E))
      continue
    if e < S:
      nr.append((s,e))
      nr.append((S,E))
      a = True
      continue
    if e >= S:
      os = min(S, s)
      oe = max(E, e)
      continue
    if s <= E:
      os = min(S, s)
      oe = max(E, e)
      continue
  if os:
    nr.append((os, oe))
  elif not a:
    nr.append((s, e))
  return nr


with open(sys.INPUTFILE, 'r') as f:
  r = []
  c = 0
  added = False
  for l in f.readlines():
    if '-' in l:
      s,e=l.split('-')
      r = ar(r,int(s),int(e))
    elif l.strip():
      v = int(l)
      for s,e in r:
        if s <= v <= e:
          c += 1
          break

  sum = 0
  for s,e in r:
    sum += (e-s+1)

  print(f'part 1 => {c}')
  print(f'part 2 => {sum}')