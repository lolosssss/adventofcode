with open('./test', 'r') as f:
  data = f.read().strip()

movements = {
  'U': [-1, 0],
  'R': [0, 1],
  'D': [1, 0],
  'L': [0, -1],
}

pds = {
  'U': [0, 1], # R
  'R': [1, 0], # D
  'D': [0, -1], # L
  'L': [-1, 0], # U
}

n2d = {
  '0': 'R',
  '1': 'D',
  '2': 'L',
  '3': 'U'
}


def get_size(lines, part2):
  wa = 0
  w_min, w_max = 0, 0
  ha = 0
  h_min, h_max = 0, 0
  for line in lines:
    d, l, cl = line.split(' ')
    if part2:
      cl = cl[2:-1]
      d = n2d[cl[-1]]
      l = int(cl[:-1], 16)
    l = int(l)
    m = movements[d]
    ha, wa = ha + m[0] * l, wa + m[1] * l
    w_min, w_max = min(wa, w_min), max(wa, w_max)
    h_min, h_max = min(ha, h_min), max(ha, h_max)
  return (h_max - h_min + 1, w_max - w_min + 1, -h_min, -w_min)


def solve(lines, part2):
  h, w, r, c = get_size(lines, part2)
  grids = [[' ' for _ in range(w)] for _ in range(h)]

  grids[r][c] = '#'
  for line in lines:
    d, l, cl = line.split(' ')
    if part2:
      cl = cl[2:-1]
      d = n2d[cl[-1]]
      l = int(cl[:-1], 16)
    l = int(l)
    m = movements[d]
    for _ in range(l):
      r, c = r + m[0], c + m[1]
      grids[r][c] = '#'

  fills = [[col for col in row] for row in grids]
  # for line in lines:
  #   d, l, cl = line.split(' ')
  #   if part2:
  #     cl = cl[2:-1]
  #     d = n2d[cl[-1]]
  #     l = int(cl[:-1], 16)
  #   l = int(l)
  #   m = movements[d]
  #   pd = pds[d]
  #   for _ in range(l):
  #     pr, pc = r + pd[0], c + pd[1]
  #     while grids[pr][pc] != '#':
  #       fills[pr][pc] = '#'
  #       pr, pc = pr + pd[0], pc + pd[1]
  #     r, c = r + m[0], c + m[1]
  #   pr, pc = r + pd[0], c + pd[1]
  #   while grids[pr][pc] != '#':
  #     fills[pr][pc] = '#'
  #     pr, pc = pr + pd[0], pc + pd[1]

  # for row in fills:
  #   print(''.join(row))
  total = 0
  for row in fills:
    for col in row:
      if col == '#':
        total += 1
  print(total)


lines = data.split('\n')
solve(lines, False)
solve(lines, True)