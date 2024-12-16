import re
from functools import reduce

with open('./input', 'r') as f:
  data = f.read().strip()

width = 101
height = 103
mw = width // 2
mh = height // 2

robots = []
for line in data.split('\n'):
  m = re.match(r'p=(-?\d*),(-?\d*) v=(-?\d*),(-?\d*)', line)
  groups = m.groups()
  pv = [int(item) for item in groups]
  robots.append([(pv[0], pv[1]), (pv[2], pv[3])])


def solve1():
  quads = [0, 0, 0, 0]
  for robot in robots:
    op, v = robot
    cp = op
    for i in range(100):
      nx = (cp[0] + v[0] + width) % width
      ny = (cp[1] + v[1] + height) % height
      np = (nx, ny)
      cp = np
    if cp[0] < mw and cp[1] < mh:
      quads[0] += 1
    elif cp[0] > mw and cp[1] < mh:
      quads[1] += 1
    elif cp[0] > mw and cp[1] > mh:
      quads[2] += 1
    elif cp[0] < mw and cp[1] > mh:
      quads[3] += 1
  return reduce(lambda i, prod: i * prod, quads)


print(f'part one: {solve1()}')


def solve2():
  pvs = robots
  for i in range(100):
    grid = [['.' for _ in range(width)] for _ in range(height)]
    nr = []
    for robot in pvs:
      cp, v = robot
      nx = (cp[0] + v[0] + width) % width
      ny = (cp[1] + v[1] + height) % height
      grid[ny][nx] = '*'
      nr.append([(nx, ny), v])
    pvs = nr
    for r in grid:
      print(''.join(r))
    print(f'second: {i}')
    input()

solve2()