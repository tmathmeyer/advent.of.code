
import sys
import functools


def part1():
  lines = [tuple(map(int, l.split(','))) for l in open(sys.INPUTFILE, 'r')]
  dists = []
  for i,s in enumerate(lines):
    for j in range(i, len(lines)):
      e = lines[j]
      d2 = sum((a-b)**2 for a,b in zip(s, e))
      if d2 != 0:
        dists.append((d2, s, e))

  dists = sorted(dists, key=lambda t: t[0])
  crs = {}
  for _,(d,s,e) in zip(range(1000), dists):
    hs = [k for k,x in crs.items() if s in x]
    he = [k for k,x in crs.items() if e in x]

    if hs and he:
      if hs[0] != he[0]:
        crs[hs[0]].update(crs[he[0]])
        del crs[he[0]]
    elif hs:
      crs[hs[0]].add(e)
    elif he:
      crs[he[0]].add(s)
    else:
      crs[s] = set([s, e])

  lens = sorted((len(x) for x in crs.values()), reverse=True)

  x = functools.reduce(int.__mul__, (l for _,l in zip(range(3), lens)))
  print(x)

def part2():
  lines = [tuple(map(int, l.split(','))) for l in open(sys.INPUTFILE, 'r')]
  dists = []
  for i,s in enumerate(lines):
    for j in range(i, len(lines)):
      e = lines[j]
      d2 = sum((a-b)**2 for a,b in zip(s, e))
      if d2 != 0:
        dists.append((d2, s, e))
  dists = sorted(dists, key=lambda t: t[0])
  crs = {}
  for _,s,e in dists:
    #print(f'Connecting {s}, {e}')

    hs = [k for k,x in crs.items() if s in x]
    he = [k for k,x in crs.items() if e in x]
    if hs and he:
      if hs[0] != he[0]:
        crs[hs[0]].update(crs[he[0]])
        del crs[he[0]]
    elif hs:
      crs[hs[0]].add(e)
    elif he:
      crs[he[0]].add(s)
    else:
      crs[s] = set([s, e])

    for _,v in crs.items():
      if len(v) == len(lines):
        print(f'CONNECTED: {s}, {e}')
        print(s[0] * e[0])
        return


part2()



