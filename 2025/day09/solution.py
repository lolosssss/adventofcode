with open('input_test', 'r') as f:
  data = f.read().strip()

tiles = [[int(v) for v in row.split(',')] for row in data.split('\n')]


def get_area(p1, p2):
  w = abs(p1[0] - p2[0]) + 1
  h = abs(p1[1] - p2[1]) + 1
  return w * h


def solve1():
  max = 0
  size = len(tiles)
  for i in range(size - 1):
    for j in range(i + 1, size):
      area = get_area(tiles[i], tiles[j])
      if area > max:
        max = area
  return max


print(f'part one: {solve1()}')


def solve2():
  size = len(tiles)
  w = max(t[0] for t in tiles)
  h = max(t[1] for t in tiles)
  grids = [['.' for _ in range(w + 1)] for _ in range(h + 1)]
  print(grids)

  return 0


print(f'part two: {solve2()}')
