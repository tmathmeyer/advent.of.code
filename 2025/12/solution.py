
import sys
import functools

C = 0
for line in open(sys.INPUTFILE, 'r').readlines():
  if 'x' in line:
    area, counts = line.strip().split(': ')
    area = functools.reduce(int.__mul__, (int(d) for d in area.split('x')))
    counts = functools.reduce(int.__add__, (int(d) for d in counts.split(' ')))
    if area > counts * 7:
      C += 1

print(C)
