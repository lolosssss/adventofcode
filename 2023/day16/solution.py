with open('./input', 'r') as f:
  data = f.read().strip()


dir_map = {
  'r\\': ['d'],
  'r/': ['u'],
  'r-': ['r'],
  'r|': ['u', 'd'],
  'l\\': ['u'],
  'l/': ['d'],
  'l-': ['l'],
  'l|': ['u', 'd'],
  'u\\': ['l'],
  'u/': ['r'],
  'u-': ['l', 'r'],
  'u|': ['u'],
  'd\\': ['r'],
  'd/': ['l'],
  'd-': ['l', 'r'],
  'd|': ['d']
}

movement = {
  'u': [-1, 0],
  'r': [0, 1],
  'd': [1, 0],
  'l': [0, -1],
}


def get_next_d(d, block):
  if block == '.':
    return [d]
  return dir_map[d + block]


def solve(grids, d, r, c):
  row = len(grids)
  col = len(grids[0])
  flags = [[0 for _ in range(col)] for _ in range(row)]
  flags[r][c] = 1
  queue = [[d, r, c]]

  cache = {}

  while len(queue) > 0:
    d, ir, ic = queue.pop(0)
    # next direction
    nds = get_next_d(d, grids[ir][ic])
    for nd in nds:
      nm = movement[nd]
      nr, nc = ir + nm[0], ic + nm[1]
      if nr in range(row) and nc in range(col):
        k = (nd, nr, nc)
        flags[nr][nc] = 1
        if k not in cache:
          queue.append([nd, nr, nc])
          cache[k] = True

  return sum(sum(row) for row in flags)


# part one
grids = [list(row) for row in data.split('\n')]
print(solve(grids, 'r', 0, 0))

# part two
row = len(grids)
col = len(grids[0])
maximum = 0
for r in range(row):
  res = solve(grids, 'r', r, 0)
  maximum = max(res, maximum)
  res = solve(grids, 'l', r, col - 1)
  maximum = max(res, maximum)
for c in range(col):
  res = solve(grids, 'd', 0, c)
  maximum = max(res, maximum)
  res = solve(grids, 'u', row - 1, c)
  maximum = max(res, maximum)
print(maximum)
