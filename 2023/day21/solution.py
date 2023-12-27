from collections import deque

with open('./input', 'r') as f:
  data = f.read().strip()


def solve(grids, start, l):
  row = len(grids)
  col = len(grids[0])
  q = deque([start])

  cache = {}
  count = 0
  pv = 0
  pvpv = 0

  for _ in range(l):
    nq = deque([])
    while q:
      p = q.popleft()
      for m in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
        np = [p[0] + m[0], p[1] + m[1]]
        if (np[0], np[1]) in cache:
          continue
        if not (0 <= np[0] < row and 0 <= np[1] < col):
          continue
        ng = grids[np[0]][np[1]]
        if ng == '#':
          continue
        cache[tuple(np)] = True
        nq.append(np)
    q = nq
    count = pvpv + len(q)
    pvpv = pv
    pv = count

  print(count)

grids = [list(line) for line in data.split('\n')]
start = [65, 65]
solve(grids, start, 64)
# solve(grids, start, 26501365)


def solve_2(grids, start, l = 26501365):
  row = len(grids)
  col = len(grids[0])
  cache = {}

  q = deque([(0, 0, start[0], start[1], 0)])
  while q:
    gr, gc, r, c, d = q.popleft()
    gr += r // row
    gc += c // col
    r = r % row
    c = c % col
    # print(gr, gc, r, c)
    if not (0 <= r < row and 0 <= c < col and grids[r][c] != '#'):
      continue
    if (gr, gc, r, c) in cache:
      continue
    if abs(gr) > 4 or abs(gc) > 4:
      continue
    cache[(gr, gc, r, c)] = d
    for dr, dc in [[-1, 0], [0, 1], [1, 0], [0, -1]]:
      q.append((gr, gc, r + dr, c + dc, d + 1))

  opt = [-3, -2, -1, 0, 1, 2, 3]
  for gr in opt:
    for r in range(row):
      for gc in opt:
        for c in range(col):
          if (gr, gc, r, c) in cache:
            print(cache[(gr, gc, r, c)], end='')
          else:
            print('#', end='')
      print('')

  # res = 0
  # for r in range(row):
  #   for c in range(col):
  #     if (0, 0, r, c) in cache:
  #       opt = [-3, -2, -1, 0, 1, 2, 3]
  #       for gr in opt:
  #         for gc in opt:
  #           cur = cache[(gr, gc, r, c)]
  #           if cur % 2 == l % 2 and cur <= l:
  #             res += 1
  #           if gr in [min(opt), max(opt)] and gc in [min(opt), max(opt)]:
  #             res += 


solve_2(grids, start, 26501365)