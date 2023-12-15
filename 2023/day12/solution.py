"""
???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1
"""

import re

with open('./input', 'r') as f:
  data = f.read().strip()

Cache = {}

# c - conditions
# b - blocks
# ic - index of conditions
# ib - index of blocks '#'
# l - length of current '#'
def recur(c, b, ic, ib, l):
  k = (ic, ib, l)
  if k in Cache:
    return Cache[k]
  if ic == len(c):
    if ib == len(b) and l == 0:
      return 1
    elif ib == len(b) - 1 and b[ib] == l:
      return 1
    return 0

  total = 0

  for d in ['.', '#']:
    if c[ic] == d or c[ic] == '?':
      if d == '.' and l == 0:
        total += recur(c, b, ic + 1, ib, l)
      elif d == '.' and l > 0 and ib < len(b) and b[ib] == l:
        total += recur(c, b, ic + 1, ib + 1, 0)
      elif d == '#':
        total += recur(c, b, ic + 1, ib, l + 1)
  Cache[k] = total
  return total

def solve(data):
  lines = data.split('\n')

  # part one
  total = 0
  for line in lines:
    conditions, *blocks = re.split(r'[ ,]', line)
    blocks = list(map(int, blocks))
    total += recur(conditions, blocks, 0, 0, 0)
    Cache.clear()
  print(total)

  # part two
  total = 0
  for line in lines:
    c, b = line.split(' ')
    c = '?'.join([c for _ in range(5)])
    b = ','.join([b for _ in range(5)])
    b = list(map(int, b.split(',')))
    total += recur(c, b, 0, 0, 0)
    Cache.clear()
  print(total)



solve(data)