with open("./input", "r") as f:
  data = f.read().strip()

mat = [list(row) for row in data.split("\n")]
row = len(mat)
col = len(mat[0])

diff = 100

for r in range(row):
  for c in range(col):
    if mat[r][c] == "S":
      start = (r, c)
    if mat[r][c] == "E":
      end = (r, c)

dirs = [
  (-1, 0),
  (0, 1),
  (1, 0),
  (0, -1),
]


def solve():
  flags = [[-1 for _ in range(col)] for _ in range(row)]
  flags[start[0]][start[1]] = 0
  cp = start
  his = set()
  count = 1
  while cp != end:
    for d in dirs:
      np = (cp[0] + d[0], cp[1] + d[1])
      if mat[np[0]][np[1]] in ['.', 'E'] and np not in his:
        his.add(np)
        flags[np[0]][np[1]] = count
        count += 1
        cp = np
  print(count)

  cheats = set()
  for r in range(1, row - 1):
    for c in range(1, col - 1):
      if flags[r][c] != -1:
        cp = (r, c)
        cv = flags[r][c]
        for d in dirs:
          np = (r + d[0], c + d[1])
          if flags[np[0]][np[1]] == -1:
            nnp = (r + 2 * d[0], c + 2 * d[1])
            if 0 <= nnp[0] < row and 0 <= nnp[1] < col and flags[nnp[0]][nnp[1]] != -1:
              v = flags[nnp[0]][nnp[1]]
              if v - cv - 2 >= diff:
                cheats.add((np[0], np[1], nnp[0], nnp[1], v - cv - 2))
  return len(cheats)


print(f"part one: {solve()}")
