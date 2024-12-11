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


def update(d, k, v):
  if k in d:
    d[k] += v
  else:
    d[k] = v


def solve2(count):
  os = dict()
  for s in stones:
    if s in os:
      os[s] += 1
    else:
      os[s] = 1

  for _ in range(count):
    ns = dict()
    for k in os.keys():
      if k == 0:
        update(ns, 1, os[k])
      elif len(str(k)) % 2 == 0:
        h = len(str(k)) // 2
        l = int(str(k)[:h])
        r = int(str(k)[h:])
        update(ns, l, os[k])
        update(ns, r, os[k])
      else:
        update(ns, k * 2024, os[k])
    os = ns

  return sum(os.values())


print(f'part two: {solve2(75)}')
