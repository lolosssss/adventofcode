with open('input', 'r') as f:
  data = f.read().strip()


manifold = [list(row) for row in data.split('\n')]
row = len(manifold)
col = len(manifold[0])
for r in range(row):
  for c in range(col):
    if manifold[r][c] == 'S':
      start = [r, c]

flags = [[False for _ in range(col)] for _ in range(row)]

def dfs(cr, cc):
  while cr < row and manifold[cr][cc] != '^':
    flags[cr][cc] = True
    cr += 1
  if cr >= row:
    return
  if manifold[cr][cc] == '^':
    if cc > 0 and flags[cr][cc-1] == False:
      dfs(cr, cc - 1)
    if cc < col - 1 and flags[cr][cc+1] == False:
      dfs(cr, cc + 1)


def solve1():
  cr, cc = start
  flags[cr + 1][cc] = True
  dfs(cr, cc)
  count = 0
  for r in range(row):
    for c in range(col):
      if manifold[r][c] == '^':
        if flags[r-1][c] == True:
          count += 1
  return count


print(f'part one: {solve1()}')

