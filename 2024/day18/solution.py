with open('./input', 'r') as f:
  data = f.read().strip()


bs = [tuple([int(i) for i in row.split(',')[::-1]]) for row in data.split('\n')]

size = 71
start = (0, 0)
end = (size - 1, size - 1)


dirs = [
  (-1, 0),
  (0, 1),
  (1, 0),
  (0, -1),
]


debug = True


def print_maze(maze, cp):
  if not debug:
    return
  nm = [[maze[r][c] for c in range(size)] for r in range(size)]
  nm[cp[0]][cp[1]] = '@'
  for r in nm:
    print(''.join(r))
  input()


def bfs(maze):
  queue = [(start[0], start[1], 0)]
  seen = set()

  while len(queue) > 0:
    r, c, acc = queue.pop(0)
    if (r, c) == end:
      return acc
    for d in dirs:
      nr, nc, nacc = r + d[0], c + d[1], acc + 1
      if 0 <= nr < size and 0 <= nc < size and maze[nr][nc] != '#':
        if (nr, nc) not in seen:
          seen.add((nr, nc))
          queue.append((nr, nc, nacc))
      
  return 999999999


def solve1():
  shortest = 999999999
  for i in range(1024, len(bs)):
    maze = [['.' for _ in range(size)] for _ in range(size)]
    for j in range(i):
      maze[bs[j][0]][bs[j][1]] = '#'
    count = bfs(maze)
    shortest = min(shortest, count)
  return shortest


print(f'part one: {solve1()}')
