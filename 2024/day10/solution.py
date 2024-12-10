with open('./input', 'r') as f:
  data = f.read().strip()

mat = [[int(c) for c in list(r)] for r in data.split('\n')]
row = len(mat)
col = len(mat[0])

dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]

def bfs(m, r, c):
  moves = [(r, c, 0)]
  seen = set()
  seen.add((r, c))
  count = 0
  while len(moves) > 0:
    cr, cc, ch = moves.pop(0)
    if ch == 9:
      count += 1
      continue
    for d in dirs:
      nr, nc, nh = cr + d[0], cc + d[1], ch + 1
      if 0 <= nr < row and 0 <= nc < col and m[nr][nc] == nh:
        if (nr, nc) not in seen:
          moves.append((nr, nc, nh))
          seen.add((nr, nc))
  return count


def solve1():
  total = 0
  for r in range(row):
    for c in range(col):
      if mat[r][c] == 0:
        total += bfs(mat, r, c)
  return total


print(f'part one: {solve1()}')


def bfs2(m, r, c):
  moves = [(r, c, 0)]
  count = 0
  while len(moves) > 0:
    cr, cc, ch = moves.pop(0)
    if ch == 9:
      count += 1
      continue
    for d in dirs:
      nr, nc, nh = cr + d[0], cc + d[1], ch + 1
      if 0 <= nr < row and 0 <= nc < col and m[nr][nc] == nh:
        moves.append((nr, nc, nh))
  return count


def solve2():
  total = 0
  for r in range(row):
    for c in range(col):
      if mat[r][c] == 0:
        total += bfs2(mat, r, c)
  return total


print(f'part two: {solve2()}')
