with open('./input', 'r') as f:
  data = f.read().strip()

stones = [int(s) for s in data.split(' ')]

def solve1(count):
  os = [s for s in stones]
  for it in range(count):
    ns = []
    for j in range(len(os)):
      if os[j] == 0:
        ns.append(1)
      elif len(str(os[j])) % 2 == 0:
        l = len(str(os[j])) // 2
        ns.append(int(str(os[j])[:l]))
        ns.append(int(str(os[j])[l:]))
      else:
        ns.append(os[j] * 2024)
    os = [s for s in ns]
  return len(os)


print(f'part one: {solve1(25)}')


def solve2(count):
  os = [s for s in stones]
  return len(os)


print(f'part two: {solve2(75)}')
