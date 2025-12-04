with open('input', 'r') as f:
  data = f.read().strip()

grid = [list(row) for row in data.split('\n')]
row = len(grid)
col = len(grid[0])


def find():
  coords = []
  for c in range(col):
    for r in range(row):
      if grid[r][c] == '@':
        rs = r - 1 if r > 0 else r
        re = r + 1 if r < row - 1 else r
        cs = c - 1 if c > 0 else c
        ce = c + 1 if c < col - 1 else c
        total = 0
        for i in range(rs, re + 1):
          for j in range(cs, ce + 1):
            if grid[i][j] == '@':
              total += 1
        if total <= 4:
          coords.append([r, c])
  return coords


def solve1():
  return len(find())


print(f'part one: {solve1()}')


def solve2():
  count = 0
  while True:
    coords = find()
    if len(coords) > 0:
      count += len(coords)
      for coord in coords:
        r, c = coord
        grid[r][c] = 'x'
    else:
      break

  return count


print(f'part two: {solve2()}')
