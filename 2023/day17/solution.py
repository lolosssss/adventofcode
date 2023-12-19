from heapq import heappush, heappop

with open('./input', 'r') as f:
  data = f.read().strip()


def solve(grids, part2):
  # accumulated value, row, col, direction, identity direction count
  q = [(0, 0, 0, -1, -1)]

  row = len(grids)
  col = len(grids[0])

  cache = {}
  minimum = 9999999999

  while q:
    acc, r, c, d, s = heappop(q)

    k = (r, c, d, s)
    if k in cache:
      continue
    cache[k] = acc

    if r == row - 1 and c == col - 1 and (not part2 or s >= 4):
      minimum = min(minimum, acc)

    for i, (dr, dc) in enumerate([[-1, 0], [0, 1], [1, 0], [0, -1]]):
      nr = r + dr
      nc = c + dc
      nd = i
      ns = s + 1 if nd == d else 1

      is_od = (nd + 2) % 4 == d
      is_valid_1 = ns <= 3
      is_valid_2 = ns <= 10 and (s >= 4 or nd == d or d == -1)
      is_valid = is_valid_2 if part2 else is_valid_1
      if 0 <= nr < row and 0 <= nc < col and not is_od and is_valid:
        if (nr, nc, nd, ns) in cache:
          continue
        heappush(q, (acc + grids[nr][nc], nr, nc, nd, ns))

  print(minimum)


grids = [list(map(int, list(row))) for row in data.split('\n')]
solve(grids, False)
solve(grids, True)
