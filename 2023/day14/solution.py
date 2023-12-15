with open('./input', 'r') as f:
  data = f.read().strip()

# rotate the grids clockwise
def rotate(grids):
  new_grids = [['' for _ in row] for row in grids]
  row = len(grids)
  col = len(grids[0])
  for i in range(row):
    for j in range(col):
      new_grids[i][j] = grids[row-j-1][i]
  return new_grids


# tilt north
def tilt(grids):
  new_grids = [row[:] for row in grids]
  row = len(grids)
  col = len(grids[0])

  for j in range(col):
    column = [row[j] for row in grids]
    i = 0
    while i < row:
      round = 0
      ni = i # new grids row index
      while i < row and column[i] != '#':
        if column[i] == 'O':
          round += 1
        i += 1
      for _ in range(round):
        new_grids[ni][j] = 'O'
        ni += 1
      while ni < i:
        new_grids[ni][j] = '.'
        ni += 1
      if i < row:
        new_grids[i][j] = '#'
      i += 1

  return new_grids


def get_total_load(grids):
  size = len(grids)
  return sum(row.count('O') * (size - i) for i, row in enumerate(grids))


def solve(data):
  grids = [list(row) for row in data.split('\n')]

  # part one
  print(get_total_load(tilt(grids)))

  #part two
  target = 1000000000
  t = 0
  cache = {}
  while t < target:
    for _ in range(4):
      grids = tilt(grids)
      grids = rotate(grids)
    key = tuple(tuple(row) for row in grids)
    if key in cache:
      cycle_l = t - cache[key]
      amt = (target - t) // cycle_l
      t += amt * cycle_l
    cache[key] = t
    t += 1

  print(get_total_load(grids))


solve(data)