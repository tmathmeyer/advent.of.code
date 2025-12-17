
import sys

def parse_target(targetstr):
  c = 0
  d = 1
  for bit in targetstr[1:-1]:
    if bit == '#':
      c += d
    d *= 2
  return c

def parsejolt(jolt):
  for bit in jolt.strip()[1:-1].split(','):
    yield int(bit)

def jolt2target(jolt):
  c = 0
  d = 1
  for n in jolt:
    if n%2 == 1:
      c += d
    d *= 2
  return c

def pb(buttonstr):
  c = 0
  for x in buttonstr[1:-1].split(','):
    c += 2**int(x)
  return c

def pb2(buttonstr):
  for x in buttonstr[1:-1].split(','):
    yield int(x)

def grps(i, v):
  if i == 1:
    for e in v:
      yield [e]
  elif 0 < i <= len(v):
    for j,q in enumerate(v):
      for sg in grps(i-1, v[j+1:]):
        yield [q] + sg

def xorx(t, v):
  for i in range(len(v)):
    for grp in grps(i, v):
      c = t
      for g in grp:
        c ^= g
      if c == 0:
        return i
  return -1

def xorx2(t, v):
  for i in range(len(v)+1):
    for grp in grps(i, v):
      c = t
      for g in grp:
        c ^= g
      if c == 0:
        yield grp

def part1():
  sum = 0
  for machine in open(sys.INPUTFILE, 'r').readlines():
    target, *buttons, _ = machine.split(' ')
    targetnum = parse_target(target)
    nb = [pb(b) for b in buttons]
    sum += xorx(targetnum, nb)
  print(sum)

import frozendict
import functools

def joltrec2(jolt, btns):
  kz = list(btns.keys())
  @functools.cache
  def solve_jolt(jolt):
    if all(v==0 for v in jolt): return 0
    if all(v%2 == 0 for v in jolt):
      return solve_jolt(tuple(v//2 for v in jolt)) * 2
    answer = 9999999999999
    for combo in xorx2(jolt2target(jolt), kz):
      nj = list(jolt)
      for btn in combo:
        for dec in btns[btn]:
          nj[dec] -= 1
      if all(v>=0 and v%2==0 for v in nj):
        nj = tuple([v//2 for v in nj])
        value = solve_jolt(nj) * 2 + len(combo)
        if value <= answer:
          answer = value
    return answer
  return solve_jolt(jolt)


def part2():
  sum = 0
  for machine in open(sys.INPUTFILE, 'r').readlines():
    _, *buttons, jolt,  = machine.split(' ')
    jolt = tuple(parsejolt(jolt))
    nb = frozendict.frozendict({pb(b):tuple(pb2(b)) for b in buttons})
    x = joltrec2(jolt, nb)
    print(x)
    sum += x
  print(sum)


part2()