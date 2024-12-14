import re

with open('./input', 'r') as f:
  data = f.read().strip()

blocks = data.split('\n\n')
limit = 100
max_prize = 10000000000000000


def cal(ma, mb, target):
  min = max_prize
  for a in range(limit):
    for b in range(limit):
      dx = a * ma[0] + b * mb[0]
      dy = a * ma[1] + b * mb[1]
      if dx == target[0] and dy == target[1]:
        p = a * 3 + b
        if p < min:
          min = p
  if min != max_prize:
    return min
  return -1


def solve1():
  total = 0
  for block in blocks:
    ba, bb, prize = block.split('\n')
    match_a = re.match(r'.*\+(\d*),.*\+(\d*)', ba)
    ma = [int(i) for i in match_a.groups()]
    match_b = re.match(r'.*\+(\d*),.*\+(\d*)', bb)
    mb = [int(i) for i in match_b.groups()]
    match_p = re.match(r'.*=(\d*),.*=(\d*)', prize)
    mp = [int(i) for i in match_p.groups()]
    res = cal(ma, mb, mp)
    if res > 0:
      total += res
  return total


print(f'part one: {solve1()}')
