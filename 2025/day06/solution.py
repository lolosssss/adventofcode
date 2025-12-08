import re

with open('input', 'r') as f:
  data = f.read()


def solve1():
  sum = 0
  problems = [re.split(r'\s+', row.strip()) for row in data.split('\n')]
  rows = len(problems)
  cols = len(problems[0])
  for i in range(cols):
    sign = problems[-1][i]
    if sign == '+':
      res = 0
      for j in range(rows - 1):
        res += int(problems[j][i])
      sum += res
    else:
      res = 1
      for j in range(rows - 1):
        res *= int(problems[j][i])
      sum += res
  return sum


print(f'part one: {solve1()}')


rows = data.split('\n')

def solve2():
  sum = 0
  rows = data.split('\n')
  rs = len(rows)
  cs = len(rows[0]) - 1
  while cs >= 0:
    nums = []
    ns = ''
    end = False
    sign = ''
    while end == False and cs >= 0:
      for i in range(rs):
        if rows[i][cs] not in ['+', '*']:
          ns += rows[i][cs]
        else:
          sign = rows[i][cs]
          end = True
      nums.append(int(ns.strip()))
      ns = ''
      cs -= 1
    if sign == '+':
      res = 0
      for n in nums:
        res += n
      sum += res
    else:
      res = 1
      for n in nums:
        res *= n
      sum += res
    cs -= 1

  return sum


print(f'part two: {solve2()}')
