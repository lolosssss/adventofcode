with open('./input', 'r') as f:
  data = f.read().strip()


ranges = list(map(lambda v: list(map(lambda i: int(i), v.split('-'))), data.split(',')))


def solve1():
  sum = 0
  for start, end in ranges:
    current = start
    while current <= end:
      size = len(str(current))
      if size % 2 != 0:
        current += 1
        continue
      half = size / 2
      low = current % 10 ** half
      high = (current - low) / 10 ** half
      if low == high:
        sum += current
      current += 1
  return sum


print(f'part one: {solve1()}')


def solve2():
  sum = 0
  for start, end in ranges:
    current = start
    origin = str(current)
    s = origin
    while current <= end:
      origin = str(current)
      s = origin
      size = len(s)
      for _ in range(size - 1):
        s = s[1:] + s[0]
        if s == origin:
          sum += current
          break
      current += 1
  return sum


print(f'part two: {solve2()}')
