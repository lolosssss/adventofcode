with open('./input', 'r') as f:
  data = f.read().strip()


ranges_str, ids_str = data.split('\n\n')
ranges = [[int(v) for v in row.split('-')] for row in ranges_str.split('\n')]
ids = [int(v) for v in ids_str.split('\n')]


def solve1():
  count = 0
  for id in ids:
    for start, end in ranges:
      if id in range(start, end+1):
        count += 1
        break
  return count


print(f'part one: {solve1()}')


def solve2():
  # important, you have to sort the list first
  ranges.sort(key=lambda item: item[0])
  merged = [ranges[0]]
  prev = ranges[0]

  for s, e in ranges[1:]:
    if s > prev[1]:
      merged.append([s, e])
      prev = [s, e]
      continue
    if e <= prev[1]:
      continue
    merged[-1] = [prev[0], e]
    prev = [prev[0], e]

  count = 0
  for s, e in merged:
    count += e - s + 1

  return count


print(f'part two: {solve2()}')
