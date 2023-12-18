import re

with open('./input', 'r') as f:
  data = f.read().strip()

def hash(s):
  total = 0
  for c in list(s):
    n = ord(c)
    total += n
    total *= 17
    total %= 256
  return total

def solve(data):
  steps = data.split(',')
  total = 0

  for step in steps:
    total += hash(step)

  return total

def solve_2(data):
  steps = data.split(',')
  total = 0

  boxes = [[] for _ in range(256)]
  for step in steps:
    l, v = re.split(r'[=-]', step)
    hl = hash(l)
    if v != '':
      find = False
      for slot in boxes[hl]:
        if slot['k'] == l:
          slot['v'] = int(v)
          find = True
      if not find:
        boxes[hl].append({'k': l, 'v': int(v)})

    else:
      boxes[hl] = list(filter(lambda i: i['k'] != l, boxes[hl]))

  for i, box in enumerate(boxes):
    for j, slot in enumerate(box):
      total += (i + 1) * (j + 1) * slot['v']
  return total

print(solve(data))
print(solve_2(data))
