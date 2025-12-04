
import grid
import sys


with open(sys.INPUTFILE, 'r') as f:
  G = [list(l.strip()) for l in f.readlines()]

C = 0
PR = None
while PR != C:
  PR = C
  NG = [[] for _ in G]
  for y,r in enumerate(G):
    for x,c in enumerate(r):
      sur = grid.gc(G,x,y,lambda c:c=='@')
      if G[y][x] == '@' and sur < 4:
        C+=1
        NG[y].append('.')
      elif G[y][x] == '@':
        NG[y].append('@')
      else:
        NG[y].append('.')
  print(C)
  G = NG

