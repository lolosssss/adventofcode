import sys
sys.setrecursionlimit(100000)

with open('./input', 'r') as f:
  lines = f.read().strip().split('\n')


movements = [
  { 'd': '^', 'm': [-1, 0] },
  { 'd': '>', 'm': [0, 1] },
  { 'd': 'v', 'm': [1, 0] },
  { 'd': '<', 'm': [0, -1] },
]


def can_move(tile, d):
  if tile == '.':
    return True
  return tile == d



def recur(grids, p, e, flags, row, col, cache):
  k = (p[0], p[1])
  # if k in cache and cache[k] == -1:
    # return -1

  maximum = -1
  for move in movements:
    d = move['d']
    m = move['m']
    nr, nc = p[0] + m[0], p[1] + m[1]
    if nr == e[0] and nc == e[1]:
      return 1
    if 0 <= nr < row and 0 <= nc < col and grids[nr][nc] != '#' and flags[nr][nc] != 1 and can_move(grids[nr][nc], d):
      flags[nr][nc] = 1
      res = recur(grids, [nr, nc], e, flags, row, col, cache)
      flags[nr][nc] = 0
      if res != -1:
        maximum = max(res, maximum)
  cache[k] = maximum

  return maximum + 1 if (maximum != -1) else -1


def solve(grids):
  s = [0, 1]
  e = [len(grids) - 1, len(grids[0]) - 2]
  flags = [[1 if c == '#' else 0 for c in r] for r in grids]
  cache = {}
  longest = recur(grids, s, e, flags, len(grids), len(grids[0]), cache)
  print(longest)


maze = [list(line) for line in lines]
# part one
solve(maze)

# part two
maze2 = [[c if c in ['#', '.'] else '.' for c in r] for r in maze]
solve(maze2)