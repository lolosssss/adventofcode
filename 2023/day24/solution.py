import re

with open('./input', 'r') as f:
  lines = f.read().strip().split('\n')


def solve(lines):
  hs = []
  for l in lines:
    px, py, pz, vx, vy, vz = list(map(int, re.split(r'[ ,@]+', l)))
    hs.append((px, py, pz, vx, vy, vz))
  size = len(hs)
  total = 0

  for i in range(size):
    for j in range(i + 1, size):
      x11 = hs[i][0]
      x12 = hs[i][0] + hs[i][3]
      x21 = hs[j][0]
      x22 = hs[j][0] + hs[j][3]
      y11 = hs[i][1]
      y12 = hs[i][1] + hs[i][4]
      y21 = hs[j][1]
      y22 = hs[j][1] + hs[j][4]

      d = (x11 - x12) * (y21 - y22) - (x21 - x22) * (y11 - y12)
      if d != 0:
        px = ((x11 * y12 - y11 * x12) * (x21 - x22) - (x11 - x12) * (x21 * y22 - y21 * x22)) / d
        py = ((x11 * y12 - y11 * x12) * (y21 - y22) - (y11 - y12) * (x21 * y22 - y21 * x22)) / d
        validA = (px > x11) == (x12 > x11)
        validB = (px > x21) == (x22 > x21)
        if 200000000000000 <= px <= 400000000000000 and 200000000000000 <= py <= 400000000000000 and validA and validB:
          total += 1
  print(total)

# min = 200000000000000
# max = 400000000000000
solve(lines)