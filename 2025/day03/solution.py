with open('input', 'r') as f:
  data = f.read().strip()

banks = [[int(char) for char in line] for line in data.split('\n')]

def solve1():
  sum = 0
  for bank in banks:
    ml= 0
    l, r = 0, 0
    while l < len(bank) - 1:
      if bank[l] > bank[ml]:
        ml = l
      l += 1
    mr = ml + 1
    r = ml + 1
    while r < len(bank):
      if bank[r] > bank[mr]:
        mr = r
      r += 1
    sum += bank[ml] * 10 + bank[mr]

  return sum


print(f'part one: {solve1()}')


def solve2():
  sum = 0
  for bank in banks:
    size = len(bank)
    mi = size # max index
    pi = -1 # preview index
    cn = 0 # current joltage
    for r in range(12):
      ci = size - (12 - r)
      mi = ci
      while ci > pi:
        if bank[ci] >= bank[mi]:
          mi = ci
        ci -= 1
      pi = mi
      cn = cn * 10 + bank[mi]
      #print(f'{mi}, {bank[mi]}, {pi}')
    sum += cn
  return sum


print(f'part two: {solve2()}')
