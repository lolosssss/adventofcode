with open('./input', 'r') as f:
  data = f.read().strip()

p1, p2 = data.split('\n\n')
ogrid = [list(row) for row in p1.split('\n')]
moves = list(p2.replace('\n', ''))
row = len(ogrid)
col = len(ogrid[0])


sr, sc = 0, 0
for r in range(row):
  for c in range(col):
    if ogrid[r][c] == '@':
      sr, sc = r, c

dirs = {
  '^': [-1, 0],
  '>': [0, 1],
  'v': [1, 0],
  '<': [0, -1],
}


def print_grid(grid, m=None):
  # for r in grid:
  #   print(''.join(r))
  # print(m)
  # input()
  return


def solve1():
  grid = [[c for c in row] for row in ogrid]
  print_grid(grid)
  cp = (sr, sc)
  for move in moves:
    m = dirs[move]
    np = (cp[0] + m[0], cp[1] + m[1])
    if grid[np[0]][np[1]] == '.':
      grid[np[0]][np[1]] = '@'
      grid[cp[0]][cp[1]] = '.'
      cp = np
      print_grid(grid)
      continue
    elif grid[np[0]][np[1]] == '#':
      print_grid(grid)
      continue
    else:
      tp = (np[0], np[1])
      while grid[tp[0]][tp[1]] not in ['.', '#']:
        tp = (tp[0] + m[0], tp[1] + m[1])
      if grid[tp[0]][tp[1]] == '#':
        print_grid(grid)
        continue
      grid[tp[0]][tp[1]] = 'O'
      grid[np[0]][np[1]] = '@'
      grid[cp[0]][cp[1]] = '.'
      cp = np
    print_grid(grid)

  total = 0
  for r in range(row):
    for c in range(col):
      if grid[r][c] == 'O':
        total += 100 * r + c
  return total

# test set result: 10092
# print(f'part one: {solve1()}')


def check_and_push(grid, cp, dir):
  if grid[cp[0]][cp[1]] == '.':
    return True
  if grid[cp[0]][cp[1]] == '#':
    return False
  if dir in ['^', 'v']:
    m = dirs[dir]
    np1 = (cp[0] + m[0], cp[1] + m[1])
    if grid[cp[0]][cp[1]] == '[':
      cp2 = (cp[0], cp[1] + 1)
      np2 = (cp[0] + m[0], cp[1] + m[1] + 1)
    if grid[cp[0]][cp[1]] == ']':
      cp2 = (cp[0], cp[1] - 1)
      np2 = (cp[0] + m[0], cp[1] + m[1] - 1)
    if grid[np1[0]][np1[1]] == '.' and grid[np2[0]][np2[1]] == '.':
      grid[np1[0]][np1[1]] = grid[cp[0]][cp[1]]
      grid[np2[0]][np2[1]] = grid[cp2[0]][cp2[1]]
      grid[cp[0]][cp[1]] = '.'
      grid[cp2[0]][cp2[1]] = '.'
      return True
    elif grid[np1[0]][np1[1]] == '#' or grid[np2[0]][np2[1]] == '#':
      return False
    else:
      canMove = check_and_push(grid, np1, dir) and check_and_push(grid, np2, dir)
      if canMove:
        grid[np1[0]][np1[1]] = grid[cp[0]][cp[1]]
        grid[np2[0]][np2[1]] = grid[cp2[0]][cp2[1]]
        grid[cp[0]][cp[1]] = '.'
        grid[cp2[0]][cp2[1]] = '.'
      return canMove
  else:
    m = dirs[dir]
    np = (cp[0] + m[0], cp[1] + m[1])
    if grid[np[0]][np[1]] == '.':
      grid[np[0]][np[1]] = grid[cp[0]][cp[1]]
      grid[cp[0]][cp[1]] = '.'
      return True
    elif grid[np[0]][np[1]] == '#':
      return False
    else:
      canMove = check_and_push(grid, np, dir)
      if canMove:
        grid[np[0]][np[1]] = grid[cp[0]][cp[1]]
        grid[cp[0]][cp[1]] = '.'
      return canMove


def solve2():
  grid = []
  for r in range(row):
    nr = []
    for c in range(col):
      if ogrid[r][c] == '#':
        nr.append('#')
        nr.append('#')
      elif ogrid[r][c] == 'O':
        nr.append('[')
        nr.append(']')
      elif ogrid[r][c] == '@':
        nr.append('@')
        nr.append('.')
      else:
        nr.append('.')
        nr.append('.')
    grid.append(nr)
  print_grid(grid)

  nrow = len(grid)
  ncol = len(grid[0])
  sr, sc = 0, 0
  for r in range(nrow):
    for c in range(ncol):
      if grid[r][c] == '@':
        sr, sc = r, c
  cp = (sr, sc)

  for move in moves:
    m = dirs[move]
    np = (cp[0] + m[0], cp[1] + m[1])
    if grid[np[0]][np[1]] == '.':
      grid[np[0]][np[1]] = '@'
      grid[cp[0]][cp[1]] = '.'
      cp = np
      print_grid(grid, move)
    elif grid[np[0]][np[1]] == '#':
      print_grid(grid, move)
    else:
      canMove = check_and_push(grid, np, move)
      if canMove:
        grid[np[0]][np[1]] = '@'
        grid[cp[0]][cp[1]] = '.'
        cp = np
      print_grid(grid, move)

  for r in grid:
    print(''.join(r))

  total = 0
  for r in range(nrow):
    for c in range(ncol):
      if grid[r][c] == '[':
        total += 100 * r + c
  return total


# test set result: 9021
print(f'part two: {solve2()}')
