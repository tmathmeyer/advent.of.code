
import sys

def part1():
  c = [tuple(map(int, l.split(','))) for l in open(sys.INPUTFILE, 'r')]
  max = 0
  for i in range(len(c)):
    for j in range(i, len(c)):
      dx = ((c[i][0] - c[j][0]) ** 2) ** 0.5 + 1
      dy = ((c[i][1] - c[j][1]) ** 2) ** 0.5 + 1
      a = dx * dy
      if a > max:
        max = a
  print(max)


def part2():
  from shapely.geometry import Polygon
  c = [tuple(map(int, l.split(','))) for l in open(sys.INPUTFILE, 'r')]
  bounds = Polygon(c)
  max = 0
  for i in range(len(c)):
    for j in range(i+1, len(c)):
      dx = ((c[i][0] - c[j][0]) ** 2) ** 0.5 + 1
      dy = ((c[i][1] - c[j][1]) ** 2) ** 0.5 + 1
      a = dx * dy
      if a > max:
        w,x,y,z = c[i], (c[i][0], c[j][1]), c[j], (c[j][0], c[i][1])
        rect = Polygon([w,x,y,z])
        if rect.within(bounds):
          print('Within bounds')
          max = a
  print(max)




part2()



