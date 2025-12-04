

def gc(G,x,y,l):
  S = 0
  if not G:
    return S
  for dx in [-1,1,0]:
    for dy in [-1,1,0]:
      if 0 <= x+dx < len(G[0]):
        if 0 <= y+dy < len(G):
          if (0,0) != (dx,dy):
            if l(G[y+dy][x+dx]):
              S+=1
  return S