with open('./input', 'r') as f:
  data = f.read().strip()

mat = [list(r) for r in data.split('\n')]
row = len(mat)
col = len(mat[0])

dirs = [
  (-1, 0),
  (0, 1),
  (1, 0),
  (0, -1),
]

def solve1():
  total = 0
  flags = [[False for _ in r] for r in mat]
  for r in range(row):
    for c in range(col):
      if flags[r][c] == False:
        ms = [(r, c, mat[r][c])]
        flags[r][c] = True
        pm = 0
        a = 1
        while len(ms) > 0:
          cr, cc, cv = ms.pop(0)
          for d in dirs:
            nr, nc = cr + d[0], cc + d[1]
            if 0 <= nr < row and 0 <= nc < col:
              if mat[nr][nc] == cv:
                if flags[nr][nc] == False:
                  ms.append((nr, nc, cv))
                  flags[nr][nc] = True
                  a += 1
              else:
                pm += 1
            else:
              pm += 1
        # print(f'{cv}, {a} * {pm} = {a * pm}')
        total += pm * a
  return total

print(f'part one: {solve1()}')
