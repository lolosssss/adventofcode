with open('./input', 'r') as f:
  data = f.read().strip()

maze = [list(row) for row in data.split('\n')]
row = len(maze)
col = len(maze[0])
start = (row - 2, 1)
end = (1, col -2)

debug = False


dirs = [
  [-1, 0],
  [0, 1],
  [1, 0],
  [0, -1],
]


def print_maze(maz, cp, flags = []):
  if not debug:
    return

  nm = [[maz[r][c] for c in range(col)] for r in range(row)]
  nm[cp[0]][cp[1]] = '@'
  signs = ['^', '>', 'v', '<']
  for r in range(row):
    for c in range(col):
      if maz[r][c] != '#':
        low = 999999999999
        for i in range(4):
          m = flags[r][c][i]
          if m != 0 and m < low:
            nm[r][c] = signs[i]
            low = m
  for r in nm:
    print(''.join(r))
  input()


def dfs(maz, flags, cp, tv, seen: set, his: list):
  if maz[cp[0]][cp[1]] == 'S':
    for h in his:
      seen.add(h)
    return
  for i in range(4):
    d = dirs[i]
    np = (cp[0] + d[0], cp[1] + d[1])
    if maz[np[0]][np[1]] != '#':
      for j in range(4):
        nv = flags[np[0]][np[1]][j]
        if nv in [tv - 1, tv - 1001]:
          his.append(np)
          dfs(maz, flags, np, nv, seen, his)
          his.pop()


def bfs(maz):
  flags = [[[0, 0, 0, 0] for c in range(col)] for r in range(row)]
  queue = [(start[0], start[1], 1, 0)]
  lowest = 999999999999
  while len(queue) > 0:
    cur = queue.pop(0)
    # print_maze(maz, cur)
    if maze[cur[0]][cur[1]] == 'E':
      if cur[3] < lowest:
        lowest = cur[3]
    for i in range(4):
      d = dirs[i]
      np = (cur[0] + d[0], cur[1] + d[1])
      if maz[np[0]][np[1]] != '#':
        nv = cur[3] + 1 if i == cur[2] else cur[3] + 1001
        if flags[np[0]][np[1]][i] != 0:
          if flags[np[0]][np[1]][i] > nv:
            next = (np[0], np[1], i, nv)
            flags[np[0]][np[1]][i] = nv
            queue.append(next)
        else:
          next = (np[0], np[1], i, nv)
          flags[np[0]][np[1]][i] = nv
          queue.append(next)
  print_maze(maz, start, flags)

  seen = set()
  his = [end]
  dfs(maz, flags, end, lowest, seen, his)

  for p in seen:
    maz[p[0]][p[1]] = 'O'
  for r in maz:
    print(''.join(r))

  return (lowest, len(seen))


def solve():
  return bfs(maze)


print(f'part (one, two): {solve()}')

