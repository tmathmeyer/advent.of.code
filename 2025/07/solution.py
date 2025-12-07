
import sys

def part1():
  with open(sys.INPUTFILE, 'r') as f:
    tps = []
    splits = 0
    for line in f.readlines():
      sol = 0
      if 'S' in line:
        tps = line.strip().replace('S', '|')
      else:
        ntp = []
        fn = None
        for T,t in zip(tps, line.strip()):
          if T in '.^':
            ntp.append(fn or '.')
            fn = None
          elif t == '.':
            ntp.append('|')
            fn = None
          elif t == '^':
            sol += 1
            ntp[-1] = '|'
            ntp.append('^')
            fn = '|'
        tps = ''.join(ntp)
        splits += sol
    print(splits)

def part2():
  i,*s = open(sys.INPUTFILE, 'r').readlines()
  x = [1 for _ in i.strip()]
  for r in s[::-1]:
    for p in range(len(x)):
      if r[p] == '^':
        x[p] = x[p-1] + x[p+1]
  for I,X in zip(i,x):
    if I == 'S': print(X)


part2()



