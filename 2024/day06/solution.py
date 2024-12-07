with open('./input', 'r') as f:
  data = f.read().strip()

mat = [list(row) for row in data.split('\n')]
row = len(mat)
col = len(mat[0])

start_x = 0
start_y = 0
for i in range(row):
  for j in range(col):
    if mat[i][j] == '^':
      start_x = i
      start_y = j

directions = [
  [-1, 0],
  [0, 1],
  [1, 0],
  [0, -1]
]

def solve1():
  count = 1
  flags = [[False for i in range(col)] for j in range(row)]
  flags[start_x][start_y] = True
  cur_x = start_x
  cur_y = start_y
  dir_idx = 0
  cur_dir = directions[dir_idx]

  while True:
    cur_x += cur_dir[0]
    cur_y += cur_dir[1]
    if cur_x < 0 or cur_x >= row or cur_y < 0 or cur_y >= col:
      break
    if mat[cur_x][cur_y] in ['.', '^']:
      if flags[cur_x][cur_y] == False:
        count += 1
        flags[cur_x][cur_y] = True
      continue
    else:
      cur_x -= cur_dir[0]
      cur_y -= cur_dir[1]
      dir_idx = (dir_idx + 1) % 4
      cur_dir = directions[dir_idx]

  return count


print(f'part one: {solve1()}')


def solve2():
  count = 0

  for r in range(row):
    for c in range(col):
      seen = set()
      if mat[r][c] in ['#', '^']:
        continue
      org = mat[r][c]
      mat[r][c] = '#'
      cx = start_x
      cy = start_y
      d = 0
      cd = directions[d]
      while True:
        cx += cd[0]
        cy += cd[1]
        if not (0 <= cx < row and 0 <= cy < col):
          break
        if (cx, cy, d) in seen:
          count += 1
          break
        if mat[cx][cy] in ['.', '^']:
          seen.add((cx, cy, d))
        else:
          cx -= cd[0]
          cy -= cd[1]
          d = (d + 1) % 4
          cd = directions[d]
      mat[r][c] = org
      print(f'{r}, {c}', end='\r')
  print('\r')

  return count


print(f'part two: {solve2()}')
