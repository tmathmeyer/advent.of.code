
import sys
import numpy as np
import os

G = {'out': []}
R = {'out': 0}
I = ['out']
for line in open(sys.INPUTFILE, 'r').readlines():
  S, Es = line.strip().split(': ')
  G[S] = list(Es.split(' '))
  R[S] = len(R)
  I.append(S)

M = np.array([[ (1 if I[x] in G[I[y]] else 0) for x in range(len(I)) ] for y in range(len(I))])

def computeTAM():
  if os.path.exists('tam.npy'):
    return np.load('tam.npy')
  S = M.copy()
  m = M
  for i in range(1, len(I)):
    print(f'multiply: {i}')
    m = m @ M
    S += m
  np.save('tam.npy', S)
  return S

def pathz(S, E):
  T = computeTAM()
  return T[R[S]][R[E]]


def part1():
  print(pathz('you', 'out'))


def part2():
  srv_fft = pathz('svr', 'fft')
  fft_dac = pathz('fft', 'dac')
  dac_out = pathz('dac', 'out')
  print(srv_fft * fft_dac * dac_out)


part2()